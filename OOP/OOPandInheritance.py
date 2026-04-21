class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Height: {self.height}")

    def get_older(self,years):
        self.age += years


p1 = Person("Alice", 30, 165)
print(p1)

p2 = Person("Bob", 25, 180)
print(p2)
print(f"Total people: {Person.amount}")

del p2
print(f"Total people: {Person.amount}")

Person.get_older(p1, 5)
print(p1)

# Inheritance
class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += (f", Salary: {self.salary}")
        return text

    def calc_yearly_salary(self):
        return self.salary * 12

w1 = Worker("Charlie", 40, 175, 3000)
print(w1)
print(f"Yearly salary: {w1.calc_yearly_salary()}")

