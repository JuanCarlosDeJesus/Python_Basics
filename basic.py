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

# Project Grade
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

# for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# using range - upto but not including the number
for i in range(10):
    print(i)
# you can use start,stop and increment
for i in range(1,11,2):
    print(i)
# for with if
for i in range(1,11):
    if i % 2 != 0:
        print(i)

# Project Fizzbuzz
"""
if # is div by 3, print fizz
if # is div by 5, pritn buzz
if # is div by 3 and 5, print fizzbuzz
"""
for i in range(100):
    if i % 3 == 0:
        if i % 5 == 0:
            print("fizzbuzz")
            continue
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
# using and
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
# using a function
def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return print("fizzbuzz")
    elif i % 3 == 0:
        return print("fizz")
    elif i % 5 == 0:
        return print("buzz")
    else:
        return print(i)

for i in range(100):
    fizzbuzz(i)

# Project function
"""
prompt a user for a name, pass it to a func and print the name
"""
def prntname(name):
    return print("Hello " + name)

name = input("What is your name? ")
prntname(name)

# Project Hangman challenge
# Create a greeting
print("Welcome to Hangman's puzzle!")
# Create a word list
words = ["hacker", "bounty", "random"]
# Randomly choose a word from the list
import random
word = random.choice(words)
print("You have 5 extra guesses!")
guess = []
for i in (word):
    # guess.append("_")
    guess += '_'
print(str(guess)[1:-1])
count = 0
game_over = False
while not game_over:
    # Ask user for a letter making sure it's in lowercase
    lttr = input("Enter a letter: ").lower()

    if lttr in word:
        # Loop throughh word to check if letter in word
        # you can use "for position in range(len(word)):"
        for i,l in enumerate(word):
            if lttr == l:
                guess[i] = l
                print(str(guess)[1:-1])
    else:
        print(f"{lttr} is not present\nYou have {5 - (count + 1)} more chances!")
        if count == 5:
            print("You lose!")
            game_over = True

    if "_"  not in guess:
        print(f"You guessed the word = {''.join(guess)}!")
        game_over = True