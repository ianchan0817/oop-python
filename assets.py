# assets.py
class Asset:
    def __init__(self, name, ticker, price):
        self.name = name  # Asset name (e.g., "Bitcoin", "Apple")
        self.ticker = ticker  # Asset ticker (e.g., "BTC", "AAPL")
        self.price = price  # Current price of the asset

    def get_info(self):
        return f"{self.name} ({self.ticker})** ${self.price}"
    