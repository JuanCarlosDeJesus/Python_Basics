class AutoTradingBot:
    def __init__(self, threshold):
        self.threshold = threshold
        self.position = None
        self.price_data = []

    def fetch_market_data(self):
        self.price_data = [69140,69150,69160,69170,69180,69190]
        return self.price_data
        print("Market data has been Fetched.")

    def latest_price(self):
        if self.price_data:
            return self.price_data[-1]
        else:
            None

    def evaluate_price(self):
        latest_price = self.latest_price()
        if latest_price < self.threshold:
            return "Sell"
        elif latest_price > self.threshold:
            return "Buy"
        else:
            return "Hold"

    def evaluate_trade(self, action):
        if self.evaluate_price() == "Sell" and self.position != "Short":
            return "Sell trade has been executed and current position is 'Short'"
        elif self.evaluate_price() == "Buy" and self.position != "Long":
            return "Buy trade has been executed and current position is 'Long'"
        elif self.evaluate_price() == "Hold":
            return "The trade is on Hold for now and current position is 'Hold'"

    def run():
        pass