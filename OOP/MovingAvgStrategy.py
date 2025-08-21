class TradingStrategy:
    def __init__(self, capital, risk_level, strategy_name):
        print("Inside TradingStrategy constructor")
        self.__capital = capital
        self.risk_level = risk_level
        self.strategy_name = strategy_name

    def execute(self):
        print("Executing a trading strategy")


class MovingAverageStrategy(TradingStrategy):
    def execute(self):
        print("Executing a moving average strategy")


# Create a MovingAverageStrategy instance
# ma_strat = MovingAverageStrategy(100000, "Medium", "Moving Average")

# Method override
# ma_strat.execute()