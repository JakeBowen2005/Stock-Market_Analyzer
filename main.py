import data_loader
import pandas as pd
import stock_metrics
import Stock_class
import Portfolio_class
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)











# ticker = input("Enter stock ticker you want information on: ")
# period = input("Enter time period you want (1d, 5d, 1mo, 6mo, 1y): ")
user_input = input("List the tickers you want Stock Anaylsis on: ")
tickers = user_input.strip().upper().split()
stocks = []

for tick in tickers:
    stocks.append(Stock_class.Stock(tick))
portfolio = Portfolio_class.Portfolio(stocks)
print(portfolio.summary())
print(f"Best Performer: {portfolio.best_performer()}")
print(f"Worst Performer: {portfolio.worst_performer()}")
        


# stock = data_loader.get_ticker(ticker)
# history = data_loader.get_history(stock, period)
# financials = data_loader.get_financials(stock)
# actions = data_loader.get_actions(stock)

# history = stock_metrics.daily_returns(history)


# print(f"{ticker} stock information\n")
# print(history.head())
# P_earnings = stock_metrics.price_to_earnings(history, financials)
# print(P_earnings)
# print(stock_metrics.total_return_percentage(history))
# print(stock_metrics.recent_return(history))
# print(stock_metrics.is_above_ma(history))








#  print(f"{ticker} Financial information\n")
# print(financials)
# print(f"{ticker} Actions")
# print(actions)
