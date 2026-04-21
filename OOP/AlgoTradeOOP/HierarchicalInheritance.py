class TradingStrategy:
    def __init__(self):
        self.capital = 100000


class MovingAverageStrategy(TradingStrategy):
    def __init__ (self):
        super().__init__()
        self.short_window = 20


class MomentumStrategy(TradingStrategy):
    def __init__(self):
        super().__init__()
        self.momentum_window = 10



# ma_strat = MovingAverageStrategy()
# mo_strat = MomentumStrategy()
# print(ma_strat.capital)
# print(mo_strat.capital)