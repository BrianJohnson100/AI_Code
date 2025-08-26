import yfinance as yf
import time

def get_stock_price(ticker):
  """
  Fetches the real-time price of a given stock ticker using yfinance.

  Args:
    ticker: The stock ticker symbol (e.g., "GOOG" for Google).

  Returns:
    The current price of the stock, or None if an error occurs.
  """
  try:
    stock = yf.Ticker(ticker)
    current_price = stock.fast_info.last_price
    return current_price
  except Exception as e:
    print(f"Error fetching price for {ticker}: {e}")
    return None

def main():
  """
  Continuously fetches and prints the real-time prices of specified stocks.
  """
  stock_tickers = {
      "GOOG": "Google",
      "META": "Meta",
      "CRM": "Salesforce",
      "CRWV": "Corebridge Financial",
      "TSLA": "TESLA, Inc.",
      "PLAY": "Dave & Buster's",
      "NVDA": "Nvidia"
  }

  while True:
    print(f"--- {time.strftime('%m/%d/%Y %H:%M:%S')} ---") # Use today's date format
    for ticker, company_name in stock_tickers.items():
      price = get_stock_price(ticker)
      if price:
        print(f"Current price of {company_name} ({ticker}): ${price:.2f}")
      else:
        print(f"Could not retrieve price for {company_name} ({ticker})")
    print("-" * 25)
    time.sleep(60)  # Update every 60 seconds (adjust as needed)

if __name__ == "__main__":
  main()
