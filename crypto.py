# crypto.py
from assets import Asset

class Crypto(Asset):
    def __init__(self, name, ticker, price, market_cap, blockchain):
        super().__init__(name, ticker, price)  # Call the parent constructor
        self.market_cap = market_cap  # Market capitalization of the crypto
        self.blockchain = blockchain  # Blockchain used (e.g., Bitcoin, Ethereum)

    def get_crypto_info(self):
        return f"{self.name} ({self.ticker}): ${self.price}, Market Cap: ${self.market_cap}, Blockchain: {self.blockchain} Blockchain"
