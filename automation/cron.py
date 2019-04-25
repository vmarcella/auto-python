import argparse
import configparser
import sys
from datetime import datetime


def main(number, other_number, output):
    """
        Main task
    """
    result = number * other_number
    print(f"[{datetime.utcnow().isoformat()}] The result is: {result}")


if __name__ == "__main__":
    # Setup the parser with help for default values
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    # Config specification
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=argparse.FileType("r"),
        help="task config file",
        default="/etc/automate.ini",
    )

    # Output destination
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=argparse.FileType("a"),
        help="The output destination for the task",
        default=sys.stdout,
    )

    # Parse our arguments
    args = parser.parse_args()

    # Load the config
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config["ARGUMENTS"]["n1"])
        args.n2 = int(config["ARGUMENTS"]["n2"])

    main(args.n1, args.n2, args.output)
