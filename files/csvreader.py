import csv
import logging


def read_csv() -> None:
    """
        Read a csv file into memory
    """
    logging.info("---READING A CSV WITH CSV READER---")
    with open("top_films.csv") as file:
        data = csv.reader(file)
        for row in data:
            logging.info(row)


def structure_csv_data() -> None:
    """
        Read a csv file into memory and then structure the data
    """
    logging.info("---READING A CSV WITH DICT READER---")
    with open("top_films.csv") as file:
        data = csv.DictReader(file)
        structured_data = [row for row in data]
        logging.info(structured_data[0])


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    read_csv()
    structure_csv_data()
