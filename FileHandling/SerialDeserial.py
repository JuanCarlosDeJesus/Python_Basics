# Serialization and Deserialization

# Serialization - process of converting python data to JSON
# Deserialization - process of converting JSON to Python data

import json

# JSON

L = [
    {
        "tradeid":"T3212","symbol":"AAPL","volume":12345
    },
    {
        "tradeid":"t3213","symbol":"MSFT","volume":22345
    }
]


# Serialization - dump
with open("trade_log.json","w") as f:
    json.dump(L,f)

# Deserialization - load
with open("trade_log.json", "r") as f:
    print(json.load(f))

# Dictionary

d = {
    "trade1":{
        "tradeid":"T3212","symbol":"AAPL","volume":12345
    },
    "trade2":{
        "tradeid":"t3213","symbol":"MSFT","volume":22345
    }
}

# Serialization - dump
with open("dict_log.json","w") as f:
    json.dump(d,f)

# Deserialization - load
with open("dict_log.json", "r") as f:
    print(json.load(f))

# Tuple

t = ("T1234","AAPL",100)

# Serialization - dump
with open("tuple_log.json","w") as f:
    json.dump(t,f)

# Deserialization - load
with open("tuple_log.json", "r") as f:
    print(tuple(json.load(f)))  # you have to specify tuple() because json will output tuple into list


# Class

class TradeSystem:
    def __init__(self, tradeid, symbol, price, volume):
        self.tradeid = tradeid
        self.symbol = symbol
        self.price = price
        self.volume = volume

objTrade = TradeSystem("T12345","BTC",125000,"100T")

import json

def show_obj(objTrade):
    if isinstance(objTrade, TradeSystem):
        return f"Trade ID: {objTrade.tradeid}, Symbol: {objTrade.symbol}, Price: {objTrade.price}, Volume: {objTrade.volume}"

# Serialization - dump
with open("obj_log.json","w") as f:
    json.dump(objTrade,f, default=show_obj)

# Deserialization - load
with open("obj_log.json", "r") as f:
    print(json.load(f))


# Pickling - python process whereby an object hierarchy is converted into a byte stream, and 
#   unpickling is the reverse

class TradeSystem:
    def __init__(self, tradeid, symbol, price, volume):
        self.tradeid = tradeid
        self.symbol = symbol
        self.price = price
        self.volume = volume

objTrade = TradeSystem("T12345","BTC",125000,"100T")

import pickle

# Serialization - dump
with open("pickle_log.pkl","wb") as f:
    pickle.dump(objTrade,f)

# Deserialization - load
with open("pickle_log.pkl", "rb") as f:
    p = pickle.load(f)

print(p.price)

# JSON vs Picke - JSON is readable pickle is binary (good if storing large files)

