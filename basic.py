# using input
print("You are targeting 10.10.10.10" + input("What ip would you like to target? "))

# take first name as and input and last name as an input and display in console "Your name is ___ ____"
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(f"Your name is {fname} {lname}.")

# create a twitter handle and bio program
print("This is a Twitter Bio program")
pet = input("What is your pet's name: ")
city = input("What city do you live in: ")
print(f"Your twitter handle is @cyber{pet} from {city}")

# Data Types
# str
print("Hello World!")
print(type("Hello World!"))
# int
print(5)
print(type(5))
# float
print(5.2)
print(type(5.2))
# Booleans True False
print(True)
print(type(False))

# Conditionals
# input 2 num and compare them
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")

# Prompt user for score and display the letter grade
grade = int(input("Enter your test score: "))

if grade >= 90:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an A+")

    else:
        print("Your grade is an A")
elif grade >= 80:
    print("Your grade is an B")
elif grade >= 70:
    print("Your grade is an C")
elif grade >= 60:
    print("Your grade is an D")
else:
    print("Your grade is an F")

