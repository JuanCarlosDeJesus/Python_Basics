from datetime import datetime
import yfinance as yf
import time


class MyTradingStrategy:
    def __init__(self, name):
        self.__name = name

    def generate_signal(self, price_data):
        print("This method is intended to Signal a HOLD status")
        return "Hold"  # means you are trying to execute a trade - Buy or Sell

    @property
    def name(self):
        return self.__name


# MyBaseObj = MyTradingStrategy("Awesome Strategy")
# MyBaseObj.generate_signal(12)
# MyBaseObj.name()


class MySmartTradingStrategy(MyTradingStrategy):
    def __init__(self, swindow, lwindow):
        self.__swindow = swindow
        self.__lwindow = lwindow
        super().__init__("My SMA Trading Strategy")

    def generate_signal(self, price_data): # overide method
        if len(price_data[-self.__lwindow:]) < self.__lwindow:
            return "Hold"
        short_avg = sum(price_data[-self.__swindow:])/self.__swindow
        long_avg = sum(price_data[-self.__lwindow:])/self.__lwindow
    
        if short_avg > long_avg:
            return "Buy"
        elif short_avg < long_avg:
            return "Sell"
        else:
            return "Hold"

    @property
    def swindow(self):
        return self.__swindow

    @property
    def lwindow(self):
        return self.__lwindow


# ObjStrat = MySmartTradingStrategy(3,5)
# ObjStrat.generate_signal([1,2,3,4,5,6,7,8,9,10])
# ObjStrat.lwindow
# ObjStrat.swindow
# ObjStrat.name


class MyTrade:
    def __init__(self, strategy_name, signal, amount):
        self.__strategy_name = strategy_name
        self.__signal = signal
        self.__amount = amount
        self.__timestamp = datetime.now()

    def execute(self):
        print(f"Executed {self.__signal} trade with the strategy {self.__strategy_name} with the amount ${self.__amount} at the tine {self.__timestamp}.")

    @property
    def strategy_name(self):
        return self.__strategy_name

    @property
    def signal(self):
        return self.__signal

    @property
    def amount(self):
        return self.__amount

    @property
    def timestamp(self):
        return self.__timestamp


# ObjStrat = MySmartTradingStrategy(3,5)
# strategy_name = ObjStrat.name
# signal = ObjStrat.generate_signal([1,2,3,4,5])
# ObjMyTrade = MyTrade(strategy_name, signal, 10000)
# ObjMyTrade.execute()

# print(ObjMyTrade.strategy_name)
# print(ObjMyTrade.signal)
# print(ObjMyTrade.amount)
# print(ObjMyTrade.timestamp)


# Mock Trading API
class MockTradingAPI:
    def __init__(self, balance):
        self.__balance = balance

    def place_order(self, trade, price):
        if trade.signal == "Buy" and self.__balance >= trade.amount * price:
            self.__balance -= trade.amount * price
            print(f"Placed a buy trade at the {price}, Remaining Balance: {self.__balance}")
        elif trade.signal == "Sell":
            self.__balance += trade.amount * price
            print(f"Placed a sell trade at the price {price}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient Balance or Invalid Signal.")

    
    @property
    def balance(self):
        return self.__balance



# trade1 = MySmartTradingStrategy(3,5)
# trade1.generate_signal([1,2,3,4,5,4,3,2,1])
# trade2 = MyTrade(strategy_name, signal, 10000)
# ObjMockApi = MockTradingAPI(10000)
# ObjMockApi.place_order(trade2, 1000)


# Finance data aggregator
class MyTradingSystem:
    def __init__(self, api, strategy, symbol):
        self.__api = api
        self.__strategy = strategy
        self.__symbol = symbol
        self.__price_data = []
    
    def fetch_price_data(self):
        data = yf.download(tickers = self.__symbol, period = '1d', interval = '1m')
        if not data.empty:
            price = data['Close'].iloc[-1]
            self.__price_data.append(price)
            if len(self.__price_data) > self.__strategy.lwindow:
                self.__strategy.lwindow.pop(0)
                print(f"Fetched new price data: {price}")
            else:
                print("No data fetched")

    def run(self):
        self.fetch_price_data()
        signal = self.__strategy.generate_signal(self.__price_data)
        print(f"Generated Signal: {signal}")
        if signal in ['Sell', 'Buy']:
            trade = MyTrade(self.__strategy.signal, 1)
            trade.execute()
            self.__api.place_order(trade, self.__price_date[-1])

    @property
    def api(self):
        return self.__api

    @property
    def strategy(self):
        return self.__strategy

    @property
    def symbol(self):
        return self.__symbol

    @property
    def balance(self):
        return self.__price_data




# data = yf.download(tickers = "AAPL", period = '1d', interval = '1m')
# data['Close'].iloc[-1]

symbol = "AAPL"
api = MockTradingAPI(balance = 10000)
strategy = MySmartTradingStrategy(3, 5)
system = MyTradingSystem(api, strategy, symbol)

for _ in range(3):
    system.run()
    print(f"Remaining balance: {api.balance}")
    time.sleep(2)