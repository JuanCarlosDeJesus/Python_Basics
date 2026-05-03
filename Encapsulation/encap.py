# Encapsulation - data hiding
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value

    @staticmethod
    def mymethod():
        print("Hello World")

Person.mymethod()

p1 = Person("Mike", 30)
print(p1.Name)
p1.mymethod()

p1.Name = "Bob"
print(p1.Name)
