import csv


STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135,
    "NFLX": 430,
}


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: ${price}")


def get_quantity(stock_name):
    while True:
        quantity = input(f"Enter quantity for {stock_name}: ").strip()

        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)

        print("Please enter a valid positive number.")


def collect_portfolio():
    portfolio = []

    print("\nEnter stock symbols one by one.")
    print("Type 'done' when you have finished adding stocks.")

    while True:
        stock_name = input("\nEnter stock symbol: ").strip().upper()

        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print("Stock not found in the price list. Try another symbol.")
            continue

        quantity = get_quantity(stock_name)
        price = STOCK_PRICES[stock_name]
        total_value = price * quantity

        portfolio.append({
            "stock": stock_name,
            "quantity": quantity,
            "price": price,
            "total": total_value,
        })

        print(f"Added {quantity} shares of {stock_name}.")

    return portfolio


def display_summary(portfolio):
    print("\nStock Portfolio Summary")
    print("-" * 52)
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<12}{'Total Value'}")
    print("-" * 52)

    total_investment = 0

    for item in portfolio:
        total_investment += item["total"]
        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<8}"
            f"${item['price']:<11}"
            f"${item['total']}"
        )

    print("-" * 52)
    print(f"Total Investment Value: ${total_investment}")

    return total_investment


def save_as_txt(portfolio, total_investment):
    with open("portfolio_report.txt", "w", encoding="utf-8") as file:
        file.write("Stock Portfolio Report\n")
        file.write("-" * 40 + "\n")

        for item in portfolio:
            file.write(
                f"{item['stock']} - "
                f"Quantity: {item['quantity']}, "
                f"Price: ${item['price']}, "
                f"Total: ${item['total']}\n"
            )

        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("Report saved as portfolio_report.txt")


def save_as_csv(portfolio, total_investment):
    with open("portfolio_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])

        for item in portfolio:
            writer.writerow([
                item["stock"],
                item["quantity"],
                item["price"],
                item["total"],
            ])

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    print("Report saved as portfolio_report.csv")


def ask_to_save(portfolio, total_investment):
    choice = input("\nDo you want to save the result? (yes/no): ").strip().lower()

    if choice not in ["yes", "y"]:
        print("Result was not saved.")
        return

    file_type = input("Save as txt or csv? ").strip().lower()

    if file_type == "txt":
        save_as_txt(portfolio, total_investment)
    elif file_type == "csv":
        save_as_csv(portfolio, total_investment)
    else:
        print("Invalid file type, so the result was not saved.")


def main():
    print("Simple Stock Portfolio Tracker")
    show_available_stocks()

    portfolio = collect_portfolio()

    if not portfolio:
        print("\nNo stocks were added to the portfolio.")
        return

    total_investment = display_summary(portfolio)
    ask_to_save(portfolio, total_investment)


if __name__ == "__main__":
    main()