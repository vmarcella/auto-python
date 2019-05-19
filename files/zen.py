import logging


def read_everything() -> None:
    """
        Read everything from the file
    """
    logging.info("---READING FILE FOR EVERYTHING---")
    with open("zen_of_python.txt") as file:
        for line in file:
            logging.info(line)


def read_should() -> None:
    """
        Look for the word should within the file
    """
    logging.info("\n---READING FILE FOR SHOULD---")
    with open("zen_of_python.txt") as file:
        for line in file:
            if "should" in line.lower():
                logging.info(line)


def read_better() -> None:
    """
        Look for the word better within the file
    """
    logging.info("---READING FILE FOR BETTER---")
    with open("zen_of_python.txt") as file:
        for line in file:
            if "better" in line.lower():
                logging.info(line)
                break


if __name__ == "__main__":
    LOG_FORMAT = "%(message)s"
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    read_everything()
    read_should()
    read_better()
