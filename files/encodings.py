"""
    Working with encoded files
"""
import logging


def read_utf8() -> None:
    """
        Read a utf-8 encoded file
    """
    with open("example_utf8.txt") as file:
        logging.info(file.read())


def read_iso() -> None:
    """
        Read an iso encoded file
    """
    # Specify the encoding of the file (default is utf-8)
    with open("example_iso.txt", encoding="iso-8859-1") as file:
        logging.info(file.read())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    read_utf8()
    read_iso()
