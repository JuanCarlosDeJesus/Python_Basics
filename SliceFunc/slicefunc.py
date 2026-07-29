# Slice Function
number = [10,90,20,55,65,70,5,15,85]

# prints the first 5 elements of the list
print(number[:5])

# prints the last 4 elements of the list
print(number[-4:])
# using slice() with None
LAST4 = slice(-4, None)
print(number[LAST4])

FIRST5 = slice(5)
print(number[FIRST5])

EVERY_OTHER = slice(0, None, 2)
print(number[EVERY_OTHER])

# using slice() with strings
my_string = "Hello, World!"
print(my_string[0:5]) 

# using slice() with steps
print(my_string[::2])  # prints every second character