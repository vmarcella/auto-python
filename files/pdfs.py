import logging

from PyPDF2 import PdfFileReader


def main() -> None:
    file = open("document-1.pdf", "rb")
    document = PdfFileReader(file)
    logging.info("---EXAMINING PDF 1 STATISTICS ---")
    logging.info(f"Amount of pages the pdf has:{document.numPages}")
    logging.info(f"Is the document encrypted: {document.isEncrypted}")
    logging.info(
        f"The document was created at: {document.documentInfo['/CreationDate']}"
    )
    logging.info(f"Document was produced by: {document.documentInfo['/Producer']}")

    logging.info("---PDF 1 PAGE 1 CONTENT---")
    logging.info(document.pages[0].extractText())
    logging.info(document.pages[1].extractText())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
