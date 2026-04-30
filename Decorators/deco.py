# Decorators are a powerful tool in Python that allows you to modify the behavior of a function without changing its code. A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.

def mydeco(function):
    def wrapper():
        print("I am decorating your function")
        function()

    return wrapper

def hello_world():
    print("Hello World!")


mydeco(hello_world)()

# This is the preferred way to use a decorator in Python, using the @ symbol:
def mydeco(function):
    def wrapper():
        print("I am decorating your function")
        function()

    return wrapper

@mydeco
def hello_world():
    print("Hello World!")

hello_world()

# If function takes arguments, you can use *args and **kwargs to pass them through the wrapper function:
def mydeco(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        function(*args, **kwargs)

    return wrapper

@mydeco
def hello(name):
    print(f"Hello {name}!")

hello("Alice")

# if you want to return a value from the decorated function, you can simply return the result of the original function call in the wrapper:
def mydeco(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function")
        return function(*args, **kwargs)

    return wrapper

@mydeco
def hello(name):
    return f"Hello {name}!"

print(hello("Alice"))

# Using decorators to log
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value

    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10,20))

# Timing functions with decorators
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds")
        return value
    return wrapper

@timed
def myfunc(x):
    result = 1
    for i in range(1,x):
        result *= i
    return result

myfunc(1000)


