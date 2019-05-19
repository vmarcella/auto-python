import logging


def read_everything() -> None:
    """
        Read everything from the file
    """
    logging.info("---READING FILE FOR EVERYTHING---\n")
    with open("zen_of_python.txt") as file:
        for line in file:
            logging.info(line)


def read_should() -> None:
    """
        Look for the word should within the file
    """
    logging.info("---READING FILE FOR SHOULD---\n")
    with open("zen_of_python.txt") as file:
        for line in file:
            if "should" in line.lower():
                logging.info(line)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    read_everything()
    read_should()
