# CodeAlpha Task 2 - Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350,
    "AMZN": 145
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("Enter Stock Symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n------ PORTFOLIO SUMMARY ------")

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_value += investment
    print(f"{stock} -> {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("-------------------------------")
print(f"Total Investment Value = ${total_value}")

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        file.write(f"{stock}: {quantity} shares = ${investment}\n")

    file.write(f"\nTotal Investment Value = ${total_value}")

print("\nPortfolio saved as portfolio_summary.txt")