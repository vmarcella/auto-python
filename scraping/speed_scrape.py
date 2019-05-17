import argparse
import concurrent.futures
import http.client
import logging
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

URL = "http://localhost:8000/"
DEFAULT_TERM = "python"


def get_links(parsed_url, page):
    """
        Get all of the links from within a page
    """
    links = []

    # Iterate through all of the elements on
    for element in page.find_all("a"):
        link = element.get("href")

        # if there is no href attribute attached
        if not link:
            continue

        # Avoid internal links
        if link.startswith("#"):
            continue

        # Transform local links into
        if not link.startswith("http"):
            domain = parsed_url.netloc
            protocol = parsed_source.scheme
            path = urljoin(parsed_url.path, link)
            link = f"{sprotocol}://{domain}{path}"

        # Skip over the link if it's not from the same domain
        if parsed_url.netloc not in link:
            continue

        # Link passes all checks, can get appended to the list
        links.append(link)

    return links


def search_text(source_link, page, text):
    """
        Search the current page for any element tha contains the
        text that we're looking for
    """
    for element in page.find_all(text=re.compile(text, flags=re.IGNORECASE)):
        logging.info(f"Link {source_link} --> {element}")


def process_link(source_link: str, text: str):
    """
        Process a link for all occurences of the word we're looking for and 
        retrieve all other links from the page
    """
    logging.info(f"Extracting links from {source_link}")
    parsed_url = urlparse(source_link)
    response = requests.get(source_link)

    if response.status_code != http.client.OK:
        logging.error(f"Error retrieving {source_link}: {response}")
        return source_link, []

    if "html" not in response.headers["Content-Type"]:
        logging.info(f"Link {source_link} is not an HTML page")
        return source_link, []
    page = BeautifulSoup(response.text, "html.parser")
    search_text(source_link, page, text)

    return source_link, get_links(parsed_url, page)
