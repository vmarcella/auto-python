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
    # Open the csv
    with open("top_films.csv") as file:
        # Reads the first row as the keys for every row that values (the values)
        data = csv.DictReader(file)
        structured_data = [row for row in data]
        logging.info(structured_data[0])


def sniff_csv() -> None:
    """
        Sniff a csv file to find it's "dialect"
    """
    logging.info("---SNIFFING THE DIALECT OF CSV---")
    # Don't read the new lines in
    with open("top_films.csv", newline="") as file:
        # Obtain the dialect from the file contents
        dialect = csv.Sniffer().sniff(file.read())

    logging.info("---READING FROM FILE WITH THE DIALECT WE FOUND---")
    with open("top_films.csv", newline="") as file:
        reader = csv.reader(file, dialect)
        for row in reader:
            logging.info(row)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    read_csv()
    structure_csv_data()
    sniff_csv()
