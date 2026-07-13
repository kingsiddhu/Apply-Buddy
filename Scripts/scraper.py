from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def get_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()
        page.goto(url, wait_until="networkidle")

        html = page.content()

        browser.close()

    return html

def scrape_by_class(html, class_name, tag=None):
    """
    Scrapes all elements with a given class from a webpage.

    
    :param str html: Target webpage
    :param str class_name: CSS class to search for
    :param str | None tag: Optional HTML tag filter (e.g. 'div', 'p')

    Returns:
        list[str]: extracted text content
    """

    
    soup = BeautifulSoup(html, "html.parser")

    # If tag is specified, narrow search; else search all tags
    if tag:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(class_=class_name)
    print()
    return [el.get_text(strip=True) for el in elements]

from bs4 import BeautifulSoup

def scrape_by_aria_label(html, aria_label, tag=None):
    """
    Scrapes all elements with a given aria label from a webpage.

    
    :param str html: Target webpage
    :param str aria_label: aria label to search for
    :param str | None tag: Optional HTML tag filter (e.g. 'div', 'p')

    Returns:
        list[str]: extracted text content
    """

    soup = BeautifulSoup(html, "html.parser")

    if tag:
        elements = soup.find_all(tag, attrs={"aria-label": aria_label})
    else:
        elements = soup.find_all(attrs={"aria-label": aria_label})

    return [el.get_text(strip=True) for el in elements]


if __name__=="__main__":
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(storage_state="auth.json")
        page = context.new_page()

        page.goto(input("link to login page: "))

        input("Log in manually, then press Enter here...")

        
        context.storage_state(path="auth.json")

        browser.close()