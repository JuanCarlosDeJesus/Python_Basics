# Any and All functions for iterable objects
# Any function returns True if any element of the iterable is true. If the iterable is empty, return False.
x = [False, False, True]


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# All function returns True if all elements of the iterable are true. If the iterable is empty, return True.
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(any(x))  # Output: True
print(all(x))  # Output: False

numbers = [2,88,46,4]  # [11,12,76,55,9,88,10]

even = lambda x: x % 2 == 0

print(any(even(num) for num in numbers))  # Output: True
print(all(even(num) for num in numbers))  # Output: False

result = [even(num) for num in numbers]

if any(result):
    print("There is at least one even number in the list.")
else:
    print("There are no even numbers in the list.") 

if all(result):
    print("All numbers in the list are even.")