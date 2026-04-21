class AutoTradingBot:

    # Static variable - access via class name
    counter = 0

    def __init__(self, stock_name, threshold):
        self.__stock_name = stock_name
        self.__threshold = threshold
        AutoTradingBot.counter += 1
        self.__position = None
        self.__price_data = []

    def getattr(self):
        return self._AutoTradingBot__threshold

    def setattr(self, new_threshold):
        if type(new_threshold) == int:
            self._AutoTradingBot__threshold = new_threshold
            return self._AutoTradingBot__threshold
        else:
            return "Enter an Integer."        

    def fetch_market_data(self):
        self.__price_data = [69140,69150,69160,69170,69180,69190]
        return self.__price_data
        print("Market data has been Fetched.")

    def latest_price(self):
        if self.__price_data:
            return self.__price_data[-1]
        else:
            None

    def evaluate_price(self):
        latest_price = self.latest_price()
        if latest_price < self.__threshold:
            return "Sell"
        elif latest_price > self.__threshold:
            return "Buy"
        else:
            return "Hold"

    def evaluate_trade(self, action):
        if self.evaluate_price() == "Sell" and self.__position != "Short":
            return "Sell trade has been executed and current position is 'Short'"
        elif self.evaluate_price() == "Buy" and self.__position != "Long":
            return "Buy trade has been executed and current position is 'Long'"
        elif self.evaluate_price() == "Hold":
            return "The trade is on Hold for now and current position is 'Hold'"

    def run():
        pass