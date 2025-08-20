class MyBaseStrategy:
    def __init__(self, name, stype):
        self.name = name
        self.stype = stype
        print("The constructor funtion of the base strategy has been initialized")

    def execute(self):
        print("The execute method of the base stratey has been executed")

class MyEMAStrategy(MyBaseStrategy):
    def __init__(self, name, stype, lwindow, swindow):
        super().__init__(name, stype)
        self.lwindow = lwindow
        self.swindow = swindow
        print("The constructor funtion of the MyEMAStrategy has been initialized")

    def evaluate(self):
        print("The evaluate method of the MyEMAStrategy has been executed")