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