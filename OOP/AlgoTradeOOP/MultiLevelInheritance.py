class TradingStrategy:
    def __init__(self):
        self.capital = 100000


class MovingAverageStrategy(TradingStrategy):
    def __init__ (self):
        super().__init__()
        self.short_window = 20


class AdvanceMovingAverageStrategy(MovingAverageStrategy):
    def __init__(self):
        super().__init__()
        self.long_window = 50

    def show(self):
        print(self.capital)
        print(self.short_window)
        print(self.long_window)


# ma_strat = AdvanceMovingAverageStrategy()
# ma_strat.show()