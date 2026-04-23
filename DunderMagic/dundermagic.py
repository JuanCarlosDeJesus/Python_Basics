# Dunder / Magic methods
# Special methods that start and end with double underscores (__) are 
# called dunder or magic methods. They allow you to define how your 
# objects behave with built-in operations, such as addition, 
# string representation, and more.

class DunderMagic:
    def __init__(self, x, y):  # Use to construct and initialize an instance of an object
        self.x = x
        self.y = y

    def __str__(self):  # Use to define the string representation of an object
        return f"DunderMagic(x={self.x}, y={self.y})"


# __add__ is used to define the behavior of the addition operator (+) for instances of the class.
str1 = "Hello, "
str2 = "world!"

result = str1 + str2  # This will call the __add__ method of the str class
result = str1.__add__(str2)  # This is equivalent to the above line

# __len__ is used to define the behavior of the len() function for instances of the class.
my_list = [1, 2, 3, 4, 5]
length = len(my_list)  # This will call the __len__ method of the list class
length = my_list.__len__()  # This is equivalent to the above line

