import logging

from PyPDF2 import PdfFileReader


def main() -> None:
    file = open("document-1.pdf", "rb")
    document = PdfFileReader(file)
    logging.info(f"Amount of pages the pdf has:{document.numPages}")
    logging.info(f"Is the document encrypted: {document.isEncrypted}")
    logging.info(
        f"The document was created at: {document.documentInfo['/CreationDate']}"
    )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
