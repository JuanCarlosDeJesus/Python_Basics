# Generators
import sys 

def mygen(x):
    for x in range(x):
        yield x ** 3

values = mygen(10000)

print(sys.getsizeof(values))

# Example 2
def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()
# print(next(values))
# print(next(values))
