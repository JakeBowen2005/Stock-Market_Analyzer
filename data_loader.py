import yfinance as yf

def get_ticker(ticker):
    return yf.Ticker(ticker)

def get_history(ticker, period):
    return ticker.history(period=period)

def get_financials(ticker):
    return ticker.financials

def get_actions(ticker):
    return ticker.actions