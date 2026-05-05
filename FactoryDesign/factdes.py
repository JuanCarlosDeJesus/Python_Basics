# Factory Design Pattern
# The Factory Design Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It promotes loose coupling by eliminating the need to bind application-specific classes into the code.
# Increase modularity and flexibility by decoupling the object creation process from the client code.
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):  # abstract class representing a person cannot create an instance

    @abstractstaticmethod
    def person_method():
        """Interface method for person"""

class Student(IPerson):

    def __init__(self):
        self.name = "Student"
       
    def person_method(self):
        print("I am a Student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Teacher"

    def person_method(self):
        print("I am a Teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Inalid Type")
        return -1

# Example usage
if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()
 