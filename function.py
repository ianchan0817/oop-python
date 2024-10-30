name = "Alice"
new_name = name.replace("A", "B")  # Creates a new string

print(name)      # Output: Alice (original string is unchanged)
print(new_name)  # Output: Blice (new string with modification)



# Function to update a dictionary in an immutable way
def update_portfolio(portfolio, stock, value):
    # Create a new dictionary with the update
    new_portfolio = portfolio.copy()
    new_portfolio[stock] = value
    return new_portfolio

def update_portfolio_mutable(portfolio, stock, value):
    portfolio[stock] = value
    return portfolio

portfolio = {"AAPL": 150, "TSLA": 700}
portfolio2 = {"META": 200, "AMAZ": 800}

new_portfolio = update_portfolio(portfolio, "GOOG", 2800)
new_portfolio2 = update_portfolio_mutable(portfolio2, "GOOG", 2800)

# print(portfolio)       
# print(new_portfolio)   
# print('************************')
print(portfolio2)      
print(new_portfolio2)  
