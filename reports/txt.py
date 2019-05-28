from datetime import datetime

TEMPLATE = """
Movies report
-------------
Date: {date}
Movies seen in the last 30 days: {num_movies}
Total minutes: {total_minutes}
"""

FILENAME_TEMPLATE = "{date}_report.txt"


def main() -> None:
    # Data to write to our output file
    data = {"date": datetime.utcnow(), "num_movies": 3, "total_minutes": 376}
    # decompress our data dictionary to use our keys as params for the string format
    report = TEMPLATE.format(**data)
    # convert the date to a prettier format and then format it into the string
    filename = FILENAME_TEMPLATE.format(date=data["date"].strftime("%Y-%m-%d"))

    # Write the report to file
    with open(filename, "w") as file:
        file.write(report)


if __name__ == "__main__":
    main()
