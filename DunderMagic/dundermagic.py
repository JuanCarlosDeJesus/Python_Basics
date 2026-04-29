# Dunder / Magic methods
# Special methods that start and end with double underscores (__) are 
# called dunder or magic methods. They allow you to define how your 
# objects behave with built-in operations, such as addition, 
# string representation, and more.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("You are being Deconstructed!")

p = Person("Carl", 55)
p.__del__()

print(p)

# Operator overload
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"X = {self.x}, Y = {self.y}"

    def __call__(self):
        return "I wuz called!"


v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2
 
print(v3.x, v3.y)  # overloading __add__ allows you to + object. you can do mult ond others
print(v3)  # activated by __repr__. you can also use __str__
v3()  # activated by __call__

