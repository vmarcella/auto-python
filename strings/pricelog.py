from decimal import Decimal

import delorean


class PriceLog:
    """
        A formal class for holding our extracted price log information
    """

    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return f"<PriceLog ({self.timestamp}, {self.product_id}, {self.price})>"

    @classmethod
    def parse(cls, text_log):
        """
            Parse from a text log with the format
            [<Timestamp>] - SALE - PRODUCT: <product id> - PRICE: $<price>
            to a pricelog object
        """
        divided_log_list = text_log.split(" - ")

        # Unpack the elements of our list into variables
        timestamp_string, _, product_string, price_string = divided_log_list

        # Use deloarean to parse our timestamp (strip off brackets to isolate
        # the ISO format time)
        timestamp = delorean.parse(timestamp_string.strip("[]"))

        # Grab the product ID (split by the colon, select
        # the second element (Id))
        product_id = int(product_string.split(":")[-1])

        # Grab the price as a decimal (split by the dolar sign, select
        # the second element)
        price = Decimal(price_string.split("$")[-1])
        return cls(timestamp, product_id, price)
