# Method Overriding

# When a subclass rovides a specific implementation of a method that is 
# already defined in the superclass

class TradingStrategy:
    def execute(self):
        print("Executing base Strategy")

class EMAStrategy(TradingStrategy):
    def execute(self):
        print("Executing EMA Strategy")

# create instance
# strat = EMAStrategy()
# strat.execute()

# Method Overloading

# When multiple methods with the same name exist in the same scope. Python does not
# support true method overloading

class TradingStrategy:
    def execute(self, times=1, name="default"):
        for i in range(times):
            print(f"Executing {name} trading strategy, run {i + 1}")

# strat = TradingStrategy()
# strat.execute()
# strat.execute(3)
# strat.execute(2. "EMA")

# Operator Overloading

# When a class defines a special method to override the behavior of it's instance

class TradingStrategy:
    def __init__(self, profit):
        self.profit = profit

    def __add__(self, other):
        return TradingStrategy(self.profit + other.profit)

    def __str__(self):
        return f"Total Profit: ${self.profit}"

# strat1 = TradingStrategy(500)
# strat2 = TradingStrategy(300)
# combined_strategy = strat1 + strat2
# print(combined_strategy)