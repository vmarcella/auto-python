"""
    The same simple task utilizing a yaml file for loading configs
"""

import argparse
import sys

import yaml


def main(number, other_number, output):
    """
        Main functionality of our task
    """
    result = number * other_number
    print(f"The result is {result}", file=output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments to our application
    parser.add_argument("-n1", type=int, help="A number", default=1)
    parser.add_argument("-n2", type=int, help="Another number", default=1)
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=argparse.FileType("r"),
        help="The YAML config file",
        default=None,
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=argparse.FileType("w"),
        help="The output file (default sys.stdout)",
        default=sys.stdout,
    )

    # Parse args
    args = parser.parse_args()

    # Load the YAML config file
    if args.config:
        config = yaml.load(args.config)
        args.n1 = config["ARGUMENTS"]["n1"]
        args.n2 = config["ARGUMENTS"]["n2"]

    main(args.n1, args.n2, args.output)
