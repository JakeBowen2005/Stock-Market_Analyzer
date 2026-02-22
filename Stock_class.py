import data_loader
import stock_metrics

class Stock:
    def __init__(self, ticker):
        # Big Data Sets
        self.ticker = data_loader.get_ticker(ticker)
        self.price_history = data_loader.get_history(self.ticker, '10y')
        self.price_history = stock_metrics.daily_returns(self.price_history)
        self.financials = data_loader.get_financials(self.ticker)
        self.actions = data_loader.get_actions(self.ticker)

        #Computed Metrics
        self.basic_stats = stock_metrics.basic_stats(self.price_history)
        self.price_to_earnings = stock_metrics.price_to_earnings(self.price_history, self.financials)
        self.total_return = stock_metrics.total_return_percentage(self.price_history)
        self.one_week_return = stock_metrics.recent_return(self.price_history, days=5)
        self.one_month_return = stock_metrics.recent_return(self.price_history, days=21)
        self.is_above_ma = stock_metrics.is_above_ma(self.price_history)

        
