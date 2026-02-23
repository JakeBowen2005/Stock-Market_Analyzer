class Portfolio:
    def __init__(self, stocks):
        """
        stocks: list of Stock objects
        """
        self.stocks = stocks
        self.tickers = [stock.ticker.ticker for stock in stocks]
        