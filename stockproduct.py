#!/usr/bin/env python3


class StockProduct:
    """The StockProduct class maintain the individual stock items."""

    def __init__(self, code, name, description, quantity, price):
        self.code = code
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
