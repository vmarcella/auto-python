"""
    A task that handles errors that occur 
"""
import argparse
import logging
import sys

# Specify our log format
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"
# Specify the debug level
LOG_LEVEL = logging.DEBUG


def main(number, other_number, output):
    """
        Main task to be executed
    """
    logging.info(f"Dividing {number} by {other_number}")
    result = number / other_number
    print(f"This is the result: {result}", file=output)


if __name__ == "__main__":
    # Create arg parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("-n1", type=int, help="A number", default=1)
    parser.add_argument("-n2", type=int, help="A non negative number", default=1)
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=argparse.FileType("w"),
        help="The output for our task",
        default=sys.stdout,
    )
    parser.add_argument(
        "-l", "--log", dest="log", type=str, help="The log file", default=None
    )

    # Parse args and then run our task
    args = parser.parse_args()

    # Check if the user specified a log file, if not output the log
    if args.log:
        logging.basicConfig(format=LOG_FORMAT, filename=args.log, level=LOG_LEVEL)
    else:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    # Attempt to divide and if it fails, log the error and quit with it.
    try:
        main(args.n1, args.n2, args.output)
    except ZeroDivisionError:
        logging.exception("There was an error running the task")
        exit(1)
