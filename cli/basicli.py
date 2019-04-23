"""
    Basic CLI application
"""
import argparse


def main(character, number):
    """
        Main function
    """
    print(character * number)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="A number")
    # Add optional parameters to our commandline program.
    parser.add_argument("-c", type=str, help="Character to print", default="#")
    parser.add_argument(
        "-U",
        action="store_true",
        default=False,
        dest="uppercase",
        help="Uppercase the character",
    )

    # Parse the args passed into our program
    args = parser.parse_args()

    # Check if the uppercase flag was used
    if args.uppercase:
        args.c = args.c.upper()

    # Call main functionality
    main(args.c, args.number)
