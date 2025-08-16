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

    def evaluate_price():
        pass

    def evaluate_trade():
        pass

    def run():
        pass