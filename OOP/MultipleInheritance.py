class TradingStrategy:
    def __init__(self):
        self.capital = 100000


class TechnicalStrategy(TradingStrategy):
    def __init__ (self):
        super().__init__()
        self.indicator = "RSI"


class FundamentalStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.metric = "PE Ratio"


class MultipleStrategy(TechnicalStrategy, FundamentalStrategy):
    def __init__(self):
        super().__init__()

    def show(self):
        print(self.capital)
        print(self.indicator)
        print(self.metric)


# create instance
# mult_strat = MultipleStrategy()
# mult_strat.show()