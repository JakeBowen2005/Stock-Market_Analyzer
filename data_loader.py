import yfinance as yf

def get_ticker(ticker):
    return yf.Ticker(ticker)

def get_history_1d(ticker):
    return ticker.history(period="1d")

def get_history_5d(ticker):
    return ticker.history(period="5d")

def get_history_1M(ticker):
    return ticker.history(period="1mo")

def get_history_6M(ticker):
    return ticker.history(period="6mo")

def get_history_1y(ticker):
    return ticker.history(period="1y")

def get_history_5y(ticker):
    return ticker.history(period="5y")

def get_history_10y(ticker):
    return ticker.history(period="10y")

def get_financials(ticker):
    return ticker.financials

def get_actions(ticker):
    return ticker.actions