"""
    Client to crawl our dummy blog post website
"""
import argparse
import http.client
import logging
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

DEFAULT_TERM = "python"


def get_links(parsed_url, page):
    """
        Get all the links to crawl
    """
    links = []

    # Iterate over all a tags within the page
    for element in page.find_all("a"):
        # Grab the actual link from the href attribute
        link = element.get("href")

        # Ensure that there is a valid hyperlink provided
        if not link:
            continue

        # Avoid all internal links
        if link.startswith("#"):
            continue

        # Enable locally referenced links to be crawled as well
        if not link.startswith("http"):
            netloc = parsed_url.netloc
            scheme = parsed_url.scheme
            # Join the current path
            path = urljoin(parsed_url.path, link)
            link = f"{scheme}://{netloc}{path}"

        # Only parse links not in the same domain
        if parsed_url.netloc not in link:
            continue

        links.append(link)

    return links


def search_text(source_link, page, text):
    """
        Search for an element with the serached text and print it
    """
    for element in page.find_all(text=re.compile(text, flags=re.IGNORECASE)):
        print(f"Link {source_link} --> {element}")


def process_link(source_link, text):
    """
        Process a link given 
    """
    logging.info(f"Extracting link from {source_link}")
    parsed_url = urlparse(source_link)
    response = requests.get(source_link)

    # Check the status code of the response
    if response.status_code != http.client.OK:
        logging.error(f"Error retrieving {source_link}: {response}")
        return []

    # Check if the response is html (Needed for search)
    if "html" not in response.headers["Content-type"]:
        logging.info(f"Link {source_link} is not an HTML page")
        return []

    # Parse the page with bs4, and then search the text for our terms
    page = BeautifulSoup(response.text, "html.parser")
    search_text(source_link, page, text)

    return get_links(parsed_url, page)


def main(base_url, to_search):
    """
        Main execution of our program
    """
    # All of the links that we've checked so far
    checked_links = set()
    # Links that we need to check
    links_to_check = [base_url]
    # The maximum amount of checks we can do
    max_checks = 10

    # While there are still links to check and we haven't
    # Exceeded our maximum checks
    while links_to_check and max_checks:
        link = links_to_check.pop(0)
        links = process_link(link, text=to_search)
        checked_links.add(link)

        # Iterate over the links
        for link_to_check in links:
            # Make sure that the link hasn't already been checked
            if link_to_check not in checked_links:
                # add the new link to checked links
                checked_links.add(link_to_check)
                links_to_check.append(link_to_check)

        max_checks -= 1


def get_arguments():
    """
        Get the arguments passed in by the user
    """
    parser = argparse.ArgumentParser()

    # Url to search through
    parser.add_argument(
        dest="url",
        type=str,
        help='Base site url. Use "http://localhost:8000/" for the recipe example',
    )

    # argument for text to search within url
    parser.add_argument("-t", type=str, help=f"Text to search, default: {DEFAULT_TERM}")

    # Get the arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    arguments = get_arguments()

    main(arguments.url, arguments.t or DEFAULT_TERM)
