"""Content extraction module for the RAG pipeline."""

import re
from typing import Tuple
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from ..config.settings import settings
from ..utils.errors import ContentExtractionError, NetworkError
from ..utils.logger import logger


def get_page_content(url: str) -> str:
    """Fetch the HTML content of a page."""
    try:
        response = requests.get(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (compatible; RAG-Pipeline/1.0; +https://example.com/bot)'
            },
            timeout=30
        )
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        raise NetworkError(f"Failed to fetch page: {str(e)}", url)


def extract_content(url: str) -> Tuple[str, str, str]:
    """
    Extract clean content from a URL, including title and section info.

    Args:
        url: URL to extract content from

    Returns:
        Tuple of (content, title, section)
    """
    logger.info(f"Extracting content from {url}")

    try:
        html_content = get_page_content(url)
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract title
        title = ""
        title_tag = soup.find('title')
        if title_tag:
            title = title_tag.get_text().strip()
        else:
            # Try h1 as title
            h1_tag = soup.find('h1')
            if h1_tag:
                title = h1_tag.get_text().strip()

        # Extract section (try to identify from URL or page structure)
        section = extract_section_from_url(url, soup)

        # Extract main content
        content = extract_main_content(soup)

        # Clean up the content
        content = clean_content(content)

        logger.debug(f"Extracted content with {len(content)} characters from {url}")

        return content, title, section

    except Exception as e:
        logger.error(f"Failed to extract content from {url}: {e}")
        raise ContentExtractionError(f"Content extraction failed: {str(e)}", url)


def extract_section_from_url(url: str, soup: BeautifulSoup) -> str:
    """Extract section/chapter information from URL or page structure."""
    # Try to get section from URL path
    parsed = urlparse(url)
    path_parts = [part for part in parsed.path.split('/') if part]

    # Common section indicators in URLs
    section_indicators = ['chapter', 'section', 'topic', 'module', 'lesson', 'part']

    for part in path_parts:
        for indicator in section_indicators:
            if indicator in part.lower():
                return part

    # If not found in URL, try to identify from page structure
    # Look for common section elements
    section_elements = soup.find_all(['nav', 'aside', 'div'], class_=re.compile(r'.*sidebar.*|.*menu.*|.*nav.*|.*toc.*', re.I))

    for elem in section_elements:
        # Look for active/breadcrumb items
        active_item = elem.find(['a', 'span'], class_=re.compile(r'.*active.*|.*current.*|.*selected.*', re.I))
        if active_item and active_item.get_text().strip():
            return active_item.get_text().strip()[:100]  # Limit length

    # Use the first path part as section if available
    if path_parts:
        return path_parts[0]

    # Default to domain if no section found
    return parsed.netloc


def extract_main_content(soup: BeautifulSoup) -> str:
    """Extract main content from BeautifulSoup object, filtering out navigation and boilerplate."""
    # Remove script and style elements
    for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
        script.decompose()

    # Look for main content containers in order of preference
    content_selectors = [
        # Docusaurus-specific selectors
        'main div.container.markdown',
        'main div.container',
        'main article',
        'main',
        'article',
        # Common content selectors
        '[role="main"]',
        '.main-content',
        '.content',
        '.post-content',
        '.article-content',
        '.entry-content',
        '.content-area',
        '.post-body',
        '.markdown',
        # Generic content containers
        'div[class*="content"]',
        'div[class*="main"]',
        'div[class*="article"]',
        'div[class*="post"]',
    ]

    main_content = None

    for selector in content_selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    # If no specific content container found, try to identify by content density
    if not main_content:
        # Look for the element with the most text content
        max_text_length = 0
        for element in soup.find_all(['div', 'section', 'article']):
            text_content = element.get_text().strip()
            if len(text_content) > max_text_length:
                max_text_length = len(text_content)
                main_content = element

    # If still no main content found, use the body
    if not main_content:
        main_content = soup.find('body')

    # Remove navigation elements that might be inside the main content
    if main_content:
        for nav in main_content.find_all(['nav', 'ul', 'ol'], class_=re.compile(r'.*nav.*|.*menu.*|.*breadcrumb.*', re.I)):
            nav.decompose()

        # Remove elements that look like they're navigation or sidebar
        for elem in main_content.find_all():
            classes = ' '.join(elem.get('class', []))
            if any(pattern in classes.lower() for pattern in ['nav', 'menu', 'sidebar', 'toc', 'breadcrumb']):
                elem.decompose()

    # Extract text content
    if main_content:
        content = main_content.get_text()
    else:
        content = soup.get_text()

    return content


def clean_content(content: str) -> str:
    """Clean extracted content by removing extra whitespace and normalizing."""
    if not content:
        return ""

    # Remove extra whitespace and normalize
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()

    # Remove common boilerplate text
    boilerplate_patterns = [
        r'Copyright \d{4}.*?',
        r'All rights reserved.*?',
        r'Privacy Policy.*?',
        r'Terms of Service.*?',
        r'Contact us.*?',
        r'Subscribe.*?',
        r'Follow us.*?',
    ]

    for pattern in boilerplate_patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)

    # Remove extra spaces created by pattern removal
    content = re.sub(r'\s+', ' ', content).strip()

    return content


if __name__ == "__main__":
    # Test the content extraction
    test_url = settings.SOURCE_URL
    try:
        content, title, section = extract_content(test_url)
        print(f"Title: {title}")
        print(f"Section: {section}")
        print(f"Content length: {len(content)} characters")
        print(f"Content preview: {content[:500]}...")
    except Exception as e:
        print(f"Error extracting content: {e}")