import pandas as pd

def daily_returns(data):
    data = data.copy()
    data["Daily Returns"] = data["Close"].pct_change()
    return data

def basic_stats(data):
    daily_return = data["Daily Returns"].dropna()

    # Total compounded return
    total_growth = (1 + daily_return).prod()

    # Number of years
    years = len(daily_return) / 252

    # True annualized return (geometric)
    annualized_return = total_growth ** (1 / years) - 1

    # Annualized volatility
    annualized_volatility = daily_return.std() * (252 ** 0.5)

    return {
        "Annualized Return": float(annualized_return),
        "Annualized Volatility": float(annualized_volatility)
    }

def price_to_earnings(history,financials):
    current_price = history["Close"].iloc[-1]

    eps = financials.loc["Diluted EPS"].iloc[0]

    pe = current_price/eps
    return pe

def total_return_percentage(history):
    end = history["Adj Close"].iloc[-1]
    start = history["Adj Close"].iloc[0]
    total_return = ((end/start)-1) * 100
    return float(total_return) 


