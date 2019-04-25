import argparse
import configparser
import sys


def main(number, other_number, output):
    result = number * other_number
    print(f"The result is {result}", file=output)


if __name__ == "__main__":
    # Create arg parser
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("-n1", type=int, help="A number", default=1)
    parser.add_argument("-n2", type=int, help="Another number", default=1)

    # argparse.Filetype will open up a file in read mode
    parser.add_argument(
        "--config", "-c", type=argparse.FileType("r"), help="config file"
    )
    parser.add_argument(
        "-o",
        dest="output",
        type=argparse.FileType("w"),
        help="output file",
        default=sys.stdout,
    )

    # parse arguments passed in
    args = parser.parse_args()

    # Check if a config file was loaded
    if args.config:
        # Create the config file parser and read in the config file
        # passed via command line
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 = int(config["ARGUMENTS"]["n1"])
        args.n2 = int(config["ARGUMENTS"]["n2"])

    main(args.n1, args.n2, args.output)
