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
            protocol = parsed_url.scheme
            path = urljoin(parsed_url.path, link)
            link = f"{protocol}://{domain}{path}"

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


def main(base_url: str, to_search: str, workers: int = 4) -> None:
    checked_links = set()
    to_check = [base_url]
    max_checks = 10

    # Start the concurrent engine and create the amount of specified workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        # While there are still links to check
        while to_check:
            # Create futures that will call process link with both the url and link to search
            futures = [
                executor.submit(process_link, url, to_search) for url in to_check
            ]
            to_check = []
            # For all executors that are completed
            for data in concurrent.futures.as_completed(futures):
                # Grab the parsed link and the new links
                link, new_links = data.result()
                checked_links.add(link)

                # Iterate through all of the new links
                for link in new_links:
                    if link not in checked_links and link not in to_check:
                        to_check.append(link)

                # Keep track of the max checks
                max_checks -= 1
                if not max_checks:
                    return


def get_arguments() -> argparse.Namespace:
    """
        Get the arguments passed in by the user.


        Returns:
            An argparse namespace object containing our parsed arguments.
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

    # Argument for the amount of workers that we should use
    parser.add_argument(
        "-w", dest="workers", type=int, help="Number of workers", default=4
    )

    # Get the arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    arguments = get_arguments()

    # Use the provided search term or default one if not provided
    main(arguments.url, arguments.t or DEFAULT_TERM, arguments.workers)
