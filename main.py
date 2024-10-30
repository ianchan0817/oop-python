# main.py
from crypto import Crypto
from stock import Stock

# Create instances using Crypto class
bitcoin = Crypto(name="Bitcoin", ticker="BTC", price=27000, market_cap=500_000_000_000, blockchain="Bitcoin")
ethereum = Crypto(name="Ethereum", ticker="ETH", price=1800, market_cap=200_000_000_000, blockchain="Ethereum")

# Create a stock instance
apple_stock = Stock(name="Apple", ticker="AAPL", price=170, exchange="NASDAQ")

# Print information
print(bitcoin.get_crypto_info())  # Bitcoin details
print(ethereum.get_crypto_info())  # Ethereum details
print(apple_stock.get_stock_info())  # Stock details

print(bitcoin.get_info())
print(ethereum.get_info())
print(apple_stock.get_info())