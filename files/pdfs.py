import logging

from PyPDF2 import PdfFileReader, utils


def main() -> None:
    # Open the first file as binary, load it into the pdf reader
    first_file = open("document-1.pdf", "rb")
    first_pdf = PdfFileReader(first_file)

    # Examine the stats of the first pdf
    logging.info("---EXAMINING PDF 1 STATISTICS ---")
    logging.info(f"Amount of pages the pdf has:{first_pdf.numPages}")
    logging.info(f"Is the document encrypted: {first_pdf.isEncrypted}")

    # Examine the document info, aka the meta data of the pdf
    logging.info(
        f"The document was created at: {first_pdf.documentInfo['/CreationDate']}"
    )
    logging.info(f"Document was produced by: {first_pdf.documentInfo['/Producer']}")

    # Extract the content of the first pdf's page
    logging.info("---PDF 1 PAGE CONTENT---")
    logging.info(first_pdf.pages[0].extractText())
    logging.info(first_pdf.pages[1].extractText())

    first_file.close()
    # End operations

    # Open the second file as binary, load it into the pdf reader
    second_file = open("document-2.pdf", "rb")
    second_pdf = PdfFileReader(second_file)
    logging.info("---NOW WORKING WITH THE SECOND PDF--")
    logging.info(f"Is the document encrypted: {second_pdf.isEncrypted}")

    # Attempt to read an encrypted pdf, have it fail, then decrypt it.
    try:
        logging.info(f"Amount of pages the pdf has:{second_pdf.numPages}")
    except utils.PdfReadError as e:
        logging.info(f"PDF Read Error: {e}")
        logging.info("Decrypting the pdf and then grabbing the number of pages")

    # Decrypt the pdf, print the output
    logging.info(f"Status of PDF decryption: {second_pdf.decrypt('automate')}")
    logging.info(f"Amount of pages the pdf has: {second_pdf.numPages}")

    # Extract the content of the second pdf's first page
    logging.info("---PDF 2 PAGE CONTENT---")
    logging.info(second_pdf.pages[0].extractText())

    second_file.close()
    # End operations for the second pdf


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    main()
