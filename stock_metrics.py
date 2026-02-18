import pandas as pd

def daily_returns(data):
    data = data.copy()
    data["Daily Returns"] = data["Close"].pct_change()
    return data

def basic_stats(data):
    daily_return = data["Daily Returns"].dropna()

    annualized_return = daily_return.mean()*252
    annualized_volatility = daily_return.std() * (252**0.5)

    return {
        "Annualized Return" : annualized_return,
        "Annualized Volatility" : annualized_volatility
    }