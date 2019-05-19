"""
    Working with encoded files
"""
import logging

from bs4 import UnicodeDammit


def read_utf8() -> None:
    """
        Read a utf-8 encoded file
    """
    logging.info("---READING UTF8 FILE---")
    with open("example_utf8.txt") as file:
        logging.info(file.read())


def read_iso() -> None:
    """
        Read an iso encoded file
    """
    logging.info("---READING ISO FILE---")
    # Specify the encoding of the file (default is utf-8)
    with open("example_iso.txt", encoding="iso-8859-1") as file:
        logging.info(file.read())


def write_utf_into_iso() -> None:
    """
        Write utf-8 encoded content into an iso encoded file
    """
    with open("example_utf8.txt") as file:
        content = file.read()

        with open("example_output_iso.txt", "w", encoding="iso-8859-1") as iso_file:
            iso_file.write(content)


def read_iso_output_file() -> None:
    """
        Read the iso output file from the write_utf_into_iso
        function
    """
    logging.info("---READING OUTPUT ISO FILE---")
    with open("example_output_iso.txt", encoding="iso-8859-1") as file:
        logging.info(file.read())


def infer_encoding() -> None:
    """
        Infer the encoding of a file with beautiful soup 4
    """
    logging.info("---INFER ENCODING OF A FILE WITH BS4---")
    with open("example_output_iso.txt", "rb") as file:
        content = file.read()

        suggestion = UnicodeDammit(content)
        logging.info(f"The inferred encoding is: {suggestion.original_encoding}")
        logging.info(f"Unicode markup: {suggestion.unicode_markup}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    read_utf8()
    read_iso()
    write_utf_into_iso()
    read_iso_output_file()
    infer_encoding()
