"""
    Working with docx files
"""

import logging

import docx


def main() -> None:
    """
        Work with docx formatted files
    """
    # Examining the document meta data. Not all docx generating programs
    # produce metadata about the files
    doc = docx.Document("document-1.docx")
    logging.info(f"title: {doc.core_properties.title}")
    logging.info(f"Key words: {doc.core_properties.keywords}")
    logging.info(f"Last modified {doc.core_properties.modified}")

    # Data of the document are stored within paragraphs, and not pages


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
