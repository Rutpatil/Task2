import requests

API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'  # Replace with your API key
portfolio = {}

def get_stock_price(symbol):
    """Fetch real-time stock price using Alpha Vantage API"""
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        price = float(data['Global Quote']['05. price'])
        return price
    except KeyError:
        print("⚠️ Invalid stock symbol or API error.")
        return None

def add_stock(symbol, quantity):
    symbol = symbol.upper()
    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {
            'quantity': quantity,
            'price': price
        }
        print(f"✅ Added {quantity} shares of {symbol} at ${price:.2f} each.")

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"❌ Removed {symbol} from portfolio.")
    else:
        print(f"⚠️ {symbol} not found in portfolio.")

def view_portfolio():
    print("\n📊 Current Portfolio:")
    total_value = 0
    for symbol, info in portfolio.items():
        current_price = get_stock_price(symbol)
        value = current_price * info['quantity']
        total_value += value
        print(f"{symbol}: {info['quantity']} shares × ${current_price:.2f} = ${value:.2f}")
    print(f"💰 Total Portfolio Value: ${total_value:.2f}")

# --- Menu ---
while True:
    print("\n==== Stock Portfolio Tracker ====")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        symbol = input("Enter stock symbol (e.g., AAPL): ")
        quantity = int(input("Enter quantity: "))
        add_stock(symbol, quantity)
    elif choice == '2':
        symbol = input("Enter stock symbol to remove: ")
        remove_stock(symbol)
    elif choice == '3':
        view_portfolio()
    elif choice == '4':
        print("👋 Exiting tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
