class MyTradingBot:
    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def Execute(self, price):
        action = self.strategy.Evaluate(price)
        return f"{self.name} is Executing a {action} action"


class AwesomeStrategy:
    def __init__(self, threshold):
        self.threshold = threshold

    def Evaluate(self, latest_price):
        if latest_price > self.threshold:
            return "BUY"
        else:
            return "SELL"
