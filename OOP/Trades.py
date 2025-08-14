class Trades:
    def __init__(self, symbol, quantity, price):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"symbol = {self.symbol}, quantity = {self.quantity}, price = {self.price}"
    
    def __str__(self):
        return f"{self.quantity} shares of {self.symbol} at {self.price}"
    
    def __add__(self, other):
        if self.symbol == other.symbol:
            new_quantity = self.quantity + other.quantity
            average_price = (self.quantity * self.price + other.quantity * other.price)/new_quantity
            return f"The latest quantity is {new_quantity} with and average price of {average_price}"
        else:
            return f"Both the symbol should be the same"
        
    def __sub__(self, other):
        if self.symbol == other.symbol:
            new_quantity = self.quantity - other.quantity
            return f"The latest quantity is {new_quantity}"
        else:
            return f"Both the symbol should be the same"
        

class Trader:
    def __init__(self, name_input, trading_style_input):
        self.name = name_input
        self.trading_style = trading_style_input

    def greet(self):
        if self.trading_style == 'day trading':
            print("Good day for trading. ", self.name)
        elif self.trading_style == 'swing trading':
            print("Hope you catch the swing, ", self.name)
        elif self.trading_style == 'scalping':
            print("Keep it fast and precise, ", self.name)
        else:
            print("Happy trading, ", self.name)