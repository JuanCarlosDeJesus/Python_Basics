class TradingStrategy:
    def __init__(self):
        self.capital = 100000


class MovingAverageStrategy(TradingStrategy):
    def __init__ (self):
        super().__init__()
        self.short_window = 20

    def show(self):
        print(self.capital)
        print(self.short_window)


# ma_strat = MovingAverageStrategy()
# ma_strat.show()