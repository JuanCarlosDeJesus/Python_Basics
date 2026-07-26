# Docstring test file

# This is a Comment
'''
This is a multi-line docstring
'''
"""
This is another multi-line docstring
"""

def docstring_function():
    """
    This function demonstrates the use of docstrings.
    It doesn't perform any operations.
    """
    pass

def addstuffwithdocstring(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (int or float): The first number to add.
    b (int or float): The second number to add.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

print(addstuffwithdocstring(3, 5))  # Output: 8 - you can see the doctstring by hovering over the function name in an IDE or using help(addstuffwithdocstring) in the Python shell.
print(help(addstuffwithdocstring))  # This will display the docstring in the console.
print(addstuffwithdocstring.__doc__)  # This will also display the docstring in the console.