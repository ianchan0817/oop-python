# stock.py
from assets import Asset

class Stock(Asset):
    def __init__(self, name, ticker, price, exchange):
        super().__init__(name, ticker, price)  # Call the parent constructor
        self.exchange = exchange  # Stock exchange (e.g., "NASDAQ", "NYSE")

    def get_stock_info(self):
        return f"{self.get_info()}, Exchange: {self.exchange}"
