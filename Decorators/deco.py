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


