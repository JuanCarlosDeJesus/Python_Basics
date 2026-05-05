# Type Hinting
#  Python is dynamically typed (not statically typed), which means that you don't have to declare the type of a variable when you create it. However, you can use type hints to indicate the expected type of a variable, function parameter, or return value.
# mypy is a static type checker for Python that can be used to check the type hints in your code.


# def myfunc(myparam: int):  # expecting an integer parameter
#     print(myparam)

# myfunc("Hello")

# if you run this code with "python typehint.py", it will work without any errors because Python is dynamically typed. However, if you run this code with "mypy typehint.py", it will give you an error because you are passing a string instead of an integer to the function.
# you can also use: python -m mypy typehint.py to check the type hints in your code.

def myfunc(myparam: int) -> str:  # expecting a return value of type string
    return f"{myparam} is an integer"

def otherfun(otherparam: str):
    print(otherparam)

otherfun(myfunc(5))  # this will work because myfunc returns a string, which is the expected type for otherfun's parameter

# in python 3.9 and later, you can use the built-in types for type hinting, such as list, dict, etc. In earlier versions of Python, you would have to import these types from the typing module.
def lstfunc(parm: list[int]):
    print(parm)
    return ""

print(lstfunc([1,2,3]))

