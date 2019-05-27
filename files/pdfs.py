import logging

from PyPDF2 import PdfFileReader, utils


def main() -> None:
    first_file = open("document-1.pdf", "rb")
    first_pdf = PdfFileReader(first_file)
    logging.info("---EXAMINING PDF 1 STATISTICS ---")
    logging.info(f"Amount of pages the pdf has:{first_pdf.numPages}")
    logging.info(f"Is the document encrypted: {first_pdf.isEncrypted}")
    logging.info(
        f"The document was created at: {first_pdf.documentInfo['/CreationDate']}"
    )
    logging.info(f"Document was produced by: {first_pdf.documentInfo['/Producer']}")

    logging.info("---PDF 1 PAGE CONTENT---")
    logging.info(first_pdf.pages[0].extractText())
    logging.info(first_pdf.pages[1].extractText())

    first_file.close()

    second_file = open("document-2.pdf", "rb")
    second_pdf = PdfFileReader(second_file)
    logging.info("---NOW WORKING WITH THE SECOND PDF--")
    logging.info(f"Is the document encrypted: {second_pdf.isEncrypted}")

    try:
        logging.info(f"Amount of pages the pdf has:{second_pdf.numPages}")
    except utils.PdfReadError as e:
        logging.info(f"PDF Read Error: {e}")
        logging.info("Decrypting the pdf and then grabbing the number of pages")

    logging.info(f"Status of PDF decryption: {second_pdf.decrypt('automate')}")
    logging.info(f"Amount of pages the pdf has: {second_pdf.numPages}")

    logging.info("---PDF 2 PAGE CONTENT---")
    logging.info(second_pdf.pages[0].extractText())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
