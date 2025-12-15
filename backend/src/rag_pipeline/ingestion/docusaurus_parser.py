"""Docusaurus-specific HTML parser for the RAG pipeline."""

import re
from typing import List, Tuple
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from ..utils.logger import logger


def is_docusaurus_page(html_content: str) -> bool:
    """
    Detect if the HTML content is from a Docusaurus-generated site.

    Args:
        html_content: Raw HTML content to analyze

    Returns:
        True if the content appears to be from a Docusaurus site
    """
    # Check for common Docusaurus indicators
    docusaurus_indicators = [
        r'docusaurus',
        r'DS-SITE-ID',
        r'__prefix',
        r'docs-',
        r'markdown',
        r'theme-',
        r'navbar',
        r'doc-sidebar',
        r'doc-page',
        r'container',
        r'doc-item',
    ]

    content_lower = html_content.lower()
    matches = 0

    for indicator in docusaurus_indicators:
        if re.search(indicator, content_lower):
            matches += 1

    # If we have at least 3 matches, it's likely a Docusaurus site
    return matches >= 3


def extract_docusaurus_content(soup: BeautifulSoup) -> str:
    """
    Extract main content from a Docusaurus-generated page.

    Args:
        soup: BeautifulSoup object of the HTML content

    Returns:
        Extracted main content as a string
    """
    # Remove common Docusaurus elements that are not part of main content
    elements_to_remove = [
        'nav[class*="navbar"]',
        'div[class*="sidebar"]',
        'div[class*="toc"]',
        'footer',
        'header',
        'aside',
        'script',
        'style'
    ]

    for selector in elements_to_remove:
        for elem in soup.select(selector):
            elem.decompose()

    # Try to find the main content area
    content_selectors = [
        # Docusaurus-specific selectors
        'main div.container.markdown',
        'main div.container',
        'main article',
        'main',
        'article',
        '[role="main"]',
        'div.main-wrapper',
        'div.doc-page',
        'div.doc-item',
        'div.markdown',
        'div.theme-doc-markdown',
        # More general selectors
        'div.content',
        'div.post-content',
        'div.article-content',
        'div.entry-content',
    ]

    main_content = None
    for selector in content_selectors:
        main_content = soup.select_one(selector)
        if main_content:
            break

    # If no specific content container found, try to identify by content density
    if not main_content:
        max_text_length = 0
        for element in soup.find_all(['div', 'section', 'article']):
            # Skip elements that look like navigation
            classes = ' '.join(element.get('class', [])).lower()
            if any(skip in classes for skip in ['nav', 'menu', 'sidebar', 'toc', 'header', 'footer']):
                continue

            text_content = element.get_text().strip()
            if len(text_content) > max_text_length:
                max_text_length = len(text_content)
                main_content = element

    if main_content:
        # Extract text and clean it
        content = main_content.get_text()
        return clean_docusaurus_content(content)
    else:
        # Fallback: extract all content and clean it
        content = soup.get_text()
        return clean_docusaurus_content(content)


def clean_docusaurus_content(content: str) -> str:
    """
    Clean Docusaurus-specific content by removing common boilerplate.

    Args:
        content: Raw content to clean

    Returns:
        Cleaned content
    """
    if not content:
        return ""

    # Normalize whitespace
    content = re.sub(r'\s+', ' ', content)
    content = content.strip()

    # Remove common Docusaurus/CMS boilerplate
    boilerplate_patterns = [
        r'Share article.*?',
        r'Edit this page.*?',
        r'Was this page helpful\?[^.]*\.',
        r'Last updated[^.]*\.',
        r'On this page.*?',
        r'In this article.*?',
        r'Continue reading.*?',
        r'Read more.*?',
        r'Next.*?',
        r'Previous.*?',
        r'Like this.*?',
        r'Tweet this.*?',
        r'Found an issue\?[^.]*\.',
    ]

    for pattern in boilerplate_patterns:
        content = re.sub(pattern, '', content, flags=re.IGNORECASE)

    # Remove extra whitespace created by removals
    content = re.sub(r'\s+', ' ', content).strip()

    return content


def extract_docusaurus_metadata(soup: BeautifulSoup, url: str) -> Tuple[str, str, List[str]]:
    """
    Extract metadata from a Docusaurus page.

    Args:
        soup: BeautifulSoup object of the HTML content
        url: URL of the page

    Returns:
        Tuple of (title, section, tags)
    """
    title = ""
    section = ""
    tags = []

    # Extract title
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.get_text().strip()
    else:
        h1_tag = soup.find('h1')
        if h1_tag:
            title = h1_tag.get_text().strip()

    # Extract section from URL path
    parsed_url = urlparse(url)
    path_parts = [part for part in parsed_url.path.split('/') if part]

    # Look for common documentation section patterns
    doc_section_indicators = [
        'docs', 'guide', 'tutorial', 'api', 'reference', 'concept',
        'chapter', 'section', 'topic', 'module', 'lesson'
    ]

    for part in path_parts:
        if part.lower() in doc_section_indicators:
            # The next part is likely the actual section
            idx = path_parts.index(part)
            if idx + 1 < len(path_parts):
                section = path_parts[idx + 1]
                break
        elif any(indicator in part.lower() for indicator in doc_section_indicators):
            section = part
            break

    # If no section found in URL, try to get from page structure
    if not section:
        # Look for breadcrumb navigation
        breadcrumb_selectors = [
            'nav[class*="breadcrumb"]',
            'ul.breadcrumbs',
            'div[class*="breadcrumb"]',
            'nav[aria-label*="breadcrumb"]'
        ]

        for selector in breadcrumb_selectors:
            breadcrumb_elem = soup.select_one(selector)
            if breadcrumb_elem:
                # Get the last item in the breadcrumb
                last_item = breadcrumb_elem.find_all(['a', 'span'])[-1] if breadcrumb_elem.find_all(['a', 'span']) else None
                if last_item:
                    section = last_item.get_text().strip()
                    break

    # Extract tags if available
    tag_selectors = [
        'meta[name="keywords"]',
        'meta[property="article:tag"]',
        'div.tags',
        'span.tag'
    ]

    for selector in tag_selectors:
        tag_elements = soup.select(selector)
        for tag_elem in tag_elements:
            if tag_elem.name == 'meta':
                content = tag_elem.get('content', '')
                if content:
                    tags.extend([tag.strip() for tag in content.split(',')])
            else:
                tags.append(tag_elem.get_text().strip())

    # Clean up tags
    tags = [tag.strip() for tag in tags if tag.strip()]

    return title, section, tags


def parse_docusaurus_page(html_content: str, url: str) -> Tuple[str, str, str, List[str]]:
    """
    Parse a Docusaurus page and extract content, title, section, and tags.

    Args:
        html_content: Raw HTML content of the page
        url: URL of the page

    Returns:
        Tuple of (content, title, section, tags)
    """
    logger.debug(f"Parsing Docusaurus page: {url}")

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract content
    content = extract_docusaurus_content(soup)

    # Extract metadata
    title, section, tags = extract_docusaurus_metadata(soup, url)

    # Clean up section name
    section = section.strip() if section else "General"

    logger.debug(f"Extracted content length: {len(content)}, title: {title}, section: {section}")

    return content, title, section, tags


if __name__ == "__main__":
    # Example usage (for testing)
    sample_html = """
    <html>
    <head>
        <title>Test Page - Docusaurus</title>
    </head>
    <body>
        <nav class="navbar">Navigation content</nav>
        <div class="sidebar">Sidebar content</div>
        <main>
            <div class="container markdown">
                <h1>Test Page</h1>
                <p>This is the main content of the page.</p>
                <p>More content here for testing purposes.</p>
            </div>
        </main>
        <footer>Footer content</footer>
    </body>
    </html>
    """

    content, title, section, tags = parse_docusaurus_page(sample_html, "https://example.com/docs/test")
    print(f"Title: {title}")
    print(f"Section: {section}")
    print(f"Content: {content}")
    print(f"Tags: {tags}")