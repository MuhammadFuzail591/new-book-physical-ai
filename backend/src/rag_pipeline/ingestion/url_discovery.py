"""URL discovery module for the RAG pipeline."""

import asyncio
import re
import time
from typing import List, Set
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from ..config.settings import settings
from ..utils.errors import NetworkError
from ..utils.logger import logger


def get_session_with_retries() -> requests.Session:
    """Create a requests session with retry strategy."""
    session = requests.Session()

    # Define retry strategy
    retry_strategy = Retry(
        total=3,  # Total number of retries
        backoff_factor=1,  # Wait time between retries (1s, 2s, 4s)
        status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry
    )

    # Mount adapter with retry strategy
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def is_valid_url(url: str, base_domain: str) -> bool:
    """Check if URL is valid and belongs to the same domain."""
    try:
        parsed = urlparse(url)
        base_parsed = urlparse(base_domain)

        # Check if it's a valid URL and belongs to the same domain
        if not all([parsed.scheme, parsed.netloc]) or parsed.scheme not in ['http', 'https']:
            return False

        # Check if it's the same domain or subdomain
        if not parsed.netloc.endswith(base_parsed.netloc):
            return False

        # Skip anchor links and non-HTML resources
        if '#' in url or any(url.lower().endswith(ext) for ext in ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.zip', '.exe', '.dmg']):
            return False

        return True
    except Exception:
        return False


def get_sitemap_urls(base_url: str) -> List[str]:
    """Try to get URLs from sitemap.xml."""
    urls = set()
    sitemap_urls = [f"{base_url}/sitemap.xml", f"{base_url}/sitemap_index.xml"]

    session = get_session_with_retries()

    for sitemap_url in sitemap_urls:
        try:
            response = session.get(sitemap_url, timeout=30)
            if response.status_code == 200:
                logger.info(f"Found sitemap at {sitemap_url}")

                # Parse sitemap
                soup = BeautifulSoup(response.content, 'xml')

                # Look for URLs in sitemap
                for loc in soup.find_all('loc'):
                    url = loc.get_text().strip()
                    if is_valid_url(url, base_url):
                        urls.add(url)

                # If this is a sitemap index, get individual sitemaps
                for sitemap in soup.find_all('sitemap'):
                    sitemap_loc = sitemap.find('loc')
                    if sitemap_loc:
                        child_sitemap_url = sitemap_loc.get_text().strip()
                        if is_valid_url(child_sitemap_url, base_url):
                            child_response = session.get(child_sitemap_url, timeout=30)
                            if child_response.status_code == 200:
                                child_soup = BeautifulSoup(child_response.content, 'xml')
                                for loc in child_soup.find_all('loc'):
                                    url = loc.get_text().strip()
                                    if is_valid_url(url, base_url):
                                        urls.add(url)

                break  # If we found a sitemap, don't try the other URLs
        except Exception as e:
            logger.warning(f"Could not fetch sitemap from {sitemap_url}: {e}")

    return list(urls)


def crawl_site_urls(base_url: str, max_urls: int = 1000) -> List[str]:
    """Crawl the site to discover URLs."""
    urls = set()
    to_visit = [base_url]
    visited = set()

    session = get_session_with_retries()

    while to_visit and len(urls) < max_urls:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        visited.add(current_url)

        try:
            response = session.get(current_url, timeout=30)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Add current URL if it's a valid page
                if is_valid_url(current_url, base_url):
                    urls.add(current_url)

                # Find all links on the page
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    absolute_url = urljoin(current_url, href)

                    if is_valid_url(absolute_url, base_url) and absolute_url not in visited and absolute_url not in to_visit:
                        to_visit.append(absolute_url)

                # Limit the number of URLs to prevent infinite crawling
                if len(to_visit) > 1000:  # Limit pending URLs
                    to_visit = to_visit[:1000]

        except Exception as e:
            logger.warning(f"Could not crawl {current_url}: {e}")

    return list(urls)


def discover_urls(source_url: str) -> List[str]:
    """
    Discover all relevant URLs from the source website using sitemap and crawling fallback.

    Args:
        source_url: Base URL of the website to discover URLs from

    Returns:
        List of discovered URLs
    """
    logger.info(f"Starting URL discovery for {source_url}")

    # First try to get URLs from sitemap
    sitemap_urls = get_sitemap_urls(source_url)
    logger.info(f"Found {len(sitemap_urls)} URLs from sitemap")

    # If sitemap didn't return many URLs, fall back to crawling
    if len(sitemap_urls) < 10:  # Arbitrary threshold
        logger.info("Sitemap returned few URLs, using crawling as fallback")
        crawled_urls = crawl_site_urls(source_url)
        logger.info(f"Found {len(crawled_urls)} URLs from crawling")

        # Combine and deduplicate URLs
        all_urls = list(set(sitemap_urls + crawled_urls))
    else:
        logger.info("Using sitemap URLs")
        all_urls = sitemap_urls

    # Filter URLs to ensure they're valid for content extraction
    valid_urls = []
    for url in all_urls:
        try:
            # Basic check for content-type in URL or path
            parsed = urlparse(url)
            path = parsed.path.lower()

            # Include pages that look like content pages
            if any(ext not in path for ext in ['.css', '.js', '.json', '.xml', '.rss']) and not any(
                pattern in path for pattern in ['/api/', '/admin/', '/dashboard/', '/login/', '/register/']
            ):
                valid_urls.append(url)
        except Exception:
            continue  # Skip invalid URLs

    logger.info(f"Discovered {len(valid_urls)} valid URLs for content extraction")
    return valid_urls


if __name__ == "__main__":
    # Test the URL discovery
    test_urls = discover_urls(settings.SOURCE_URL)
    print(f"Discovered {len(test_urls)} URLs:")
    for url in test_urls[:10]:  # Print first 10
        print(f"  - {url}")
    if len(test_urls) > 10:
        print(f"  ... and {len(test_urls) - 10} more")