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


class HybridStrategy(TechnicalStrategy, FundamentalStrategy):
    def __init__(self):
        TechnicalStrategy.__init__(self)
        FundamentalStrategy.__init__(self)

    def show(self):
        print(self.capital)
        print(self.indicator)
        print(self.metric)

# create instance
# hybrid_strat = HybridStrategy()
# hybrid_strat.show()