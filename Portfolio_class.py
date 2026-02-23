class Portfolio:
    def __init__(self, stocks):
        """
        stocks: list of Stock objects
        """
        self.stocks = stocks
        self.tickers = [stock.ticker.ticker for stock in stocks]

    def best_performer(self):
        best = max(self.stocks, key=lambda s: s.total_return)
        return best.name

    def worst_performer(self):
        worst = min(self.stocks, key=lambda s: s.total_return)
        return worst.name

    def summary(self):
        print("Portfolio Summary")
        print("------------------")
        for stock in self.stocks:
            print(f"{stock.ticker.ticker}")
            print(f"  Annual Return: {stock.basic_stats['Annualized Return']:.2%}")
            print(f"  Volatility: {stock.basic_stats['Annualized Volatility']:.2%}")
            print(f"  Total Return (10Y): {stock.total_return:.2f}%")
            print()