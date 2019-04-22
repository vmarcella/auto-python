"""
    Working with template strings
"""
from decimal import Decimal

import delorean
from parse import parse

from pricelog import PriceLog


def create_formatted_table():
    """
        Create a formatted string table
    """
    sales_data = [(1000, 10), (2000, 17), (2500, 170), (2500, -170)]

    print("REVENUE | PROFIT | PERCENT")
    row_template = "{revenue:>7,} | {profit:>+6} | {percent:>7.2%}"

    for revenue, profit in sales_data:
        row = row_template.format(
            revenue=revenue, profit=profit, percent=(profit / revenue)
        )
        print(row)


def transform_report():
    """
        The output report needs to...
        Eliminate any references to numbers
        be properly formatted by adding a new line after each period
        justified with 80 characteers
        transformed into ASCII for compatibility reasons
    """

    input_text = """
        AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTAÑACORP
        HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE
        WITH THE OBJECTIVES FOR THE YEAR. THE MAIN DRIVER OF THE SALES HAS
        BEEN
        THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING
        DEPARTMENT.
        OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH
        THE BOARD
        CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS
        SATISFACTORY
        AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD
        EXPECTS
        AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS.
    """

    # Split our text up by words
    words = input_text.split()

    # Replace all digits with X. (we evaluate each character in a word and then join
    # the word back together at the end)
    redacted = [
        "".join("X" if char.isdigit() else char for char in word) for word in words
    ]

    # Convert all words into ascii characters. We use errors to force the replacement if
    # we encounter a non ascii character.
    ascii_text = [
        word.encode("ascii", errors="replace").decode("ascii") for word in redacted
    ]

    # format the words that end with to have new lines
    new_lines = [word + "\n" if word.endswith(".") else word for word in ascii_text]

    line_size = 80
    lines = []
    line = ""

    # Construct the newly formatted lines that terminate when they're longer than 80 chars
    # or when they contain a \n character.
    for word in new_lines:
        if line.endswith("\n") or len(line) + len(word) > line_size:
            lines.append(line)
            line = ""
        line = line + " " + word

    # Apply title casing to all lines, and then join the string back together
    # for output use!
    lines = [line.title() for line in lines]
    result_text = "\n".join(lines)

    return result_text


def extract_data_from_structure():
    """
        Extracting useful information out of a structured string 
        into python as native python types/objects we can work with
    """

    # our structured log
    text_log = "[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99"
    # Our log divided into a list (separated by dashes and spaces)
    divided_log_list = text_log.split(" - ")

    # Unpack the elements of our list into variables
    timestamp_string, _, product_string, price_string = divided_log_list

    # Use deloarean to parse our timestamp (strip off
    # brackets to isolate the ISO format time)
    timestamp = delorean.parse(timestamp_string.strip("[]"))

    # Grab the product ID (split by the colon, select the second element (Id))
    product_id = int(product_string.split(":")[-1])

    # Grab the price as a decimal (split by the dolar sign,
    # select the second element)
    price = Decimal(price_string.split("$")[-1])

    return timestamp, product_id, price


def extract_data_with_parse():
    """
        Using the library parse to extract data from strings given a log
        and the format of it including what you'd like to extract
    """

    # custom function for handling the price
    def price(string):
        return Decimal(string)

    # Same log we've been using for every other method of extraction
    text_log = "[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99"

    # Specify the format of the log we're extracting data from
    # (like a format string)
    log_format = "[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}"

    # Parse the text_log using log_format and a dictionary mapping our custom function
    # to price
    result = parse(log_format, text_log, {"price": price})

    print(result)
    print(result["date"])
    print(result["product"])
    print(result["price"])


# Create a formatted table
print("\nCreating a fromatted table")
create_formatted_table()

# Grab our transformed report
print("\nTransforming a poorly formatted memo")
print(transform_report())

# Grab our extracted information
print("\nExtracting information from a string straight into variables")
print(extract_data_from_structure())

# Use our PriceLog object to parse the same string of text
print("\nExtracting information from a string with our own object")
log = "[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99"
print(PriceLog.parse(log))

print("\nWorking with parse to extract information")
extract_data_with_parse()
