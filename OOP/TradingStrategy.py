class TradingStrategy:
    def __init__(self, symbol, amount):
        self.symbol = symbol
        self.amount = amount
        self.position = 0

    def Buy(self, price, quantity):
        if self.amount >= price * quantity:
            self.position += quantity
            self.amount -= price * quantity
            print(f"Successfully purchased {quantity} shares of {self.symbol} at ${price}")
        else:
            print("Not enough amount to proceed with the trade")

    def Sell(self, price, quantity):
        if self.position >= quantity:
            self.position -= quantity
            self.amount += price + quantity
            print(f"Successfully sold {quantity} shares of {self.symbol} at ${price}")
        else:
            print("Currently no shares to sell")
    
    def Status(self):
        print(f"Current position {self.position} of {self.symbol} shares")
        print(f"Remaining Amount ${self.amount}")