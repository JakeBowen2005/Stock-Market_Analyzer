import data_loader
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


ticker = "AAPL"

stock = data_loader.get_ticker(ticker)
history = stock.history(period="5d")
print("One day history of Apple")
# print(history)
print(history["Open"])