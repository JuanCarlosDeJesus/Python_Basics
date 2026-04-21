# Operator overloading
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return (f"X: {self.x}, Y: {self.y}")

v1 = Vector(2,5)
v2 = Vector(6,3)

print(v1)
print(v2)
v3 = v1+v2
print(v3)