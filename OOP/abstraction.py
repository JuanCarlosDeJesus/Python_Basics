
# Abstraction is a concept in OOP where you define abstrac class and method
# that are meant to be overriden in derived classes. 

from abc import ABC, abstractmethod  # ABC means abstract class

# do not make an instance or the abstract class only the child class
class TradingApp(ABC):
    def connect(self):
        print("Connected to trading server")

    # Abstract class must have at least 1 abstract method
    @abstractmethod
    def strategy(self):
        pass

    @abstractmethod
    def execute_trade(self):
        pass

class EMATradingApp(TradingApp):
    def mobile_login(self):
        print("Logged into mobile trading app")

    def strategy(self):
        print("Using EMA trading strategy")

    def execute_trade(self):
        print("Executing trade based on EMA Strategy")

# app = EMATradingApp()
# app.connect()
# app.mobile_login()
# app.strategy()
# app.execute_trade()