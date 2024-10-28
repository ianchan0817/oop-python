def get_asset_details(name, ticker, price, market_cap=None, blockchain=None, exchange=None):
    asset_info = f"{name} ({ticker}): ${price}"  # Basic asset info

    if blockchain:  # Check if it's a cryptocurrency
        market_cap_info = f"Market Cap: ${market_cap}"
        blockchain_info = f"Blockchain: {blockchain}"
        full_info = f"{asset_info}, {market_cap_info}, {blockchain_info}"
    else:  # Assume it's a stock
        exchange_info = f"Exchange: {exchange}"
        full_info = f"{asset_info}, {exchange_info}"

    print(full_info)  # Print the full info
# Define asset details
bitcoin = {
    "name": "Bitcoin",
    "ticker": "BTC",
    "price": 27000,
    "market_cap": 500_000_000_000,
    "blockchain": "Bitcoin Blockchain"
}

ethereum = {
    "name": "Ethereum",
    "ticker": "ETH",
    "price": 1800,
    "market_cap": 200_000_000_000,
    "blockchain": "Ethereum Blockchain"
}

apple_stock = {
    "name": "Apple",
    "ticker": "AAPL",
    "price": 170,
    "exchange": "NASDAQ"
}

# Function to get details for either crypto or stock


# Call the function for each asset directly
get_asset_details("Bitcoin", "BTC", 27000, market_cap=500_000_000_000, blockchain="Bitcoin Blockchain")
get_asset_details("Ethereum", "ETH", 1800, market_cap=200_000_000_000, blockchain="Ethereum Blockchain")
get_asset_details("Apple", "AAPL", 170, exchange="NASDAQ")
