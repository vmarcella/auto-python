from decimal import Decimal

import delorean
from parse import parse


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

        # price formatting func
        def price(string):
            return Decimal(string)

        # isodate formatting func
        def isodate(string):
            return delorean.parse(string)

        log_format = (
            "[{timestamp:isodate}] - SALE - PRODUCT: {product:d} - "
            "PRICE: ${price:price}"
        )

        formats = {"price": price, "isodate": isodate}
        result = parse(log_format, text_log, formats)
        return cls(result["timestamp"], result["product"], result["price"])
