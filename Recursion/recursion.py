# Recursive

n = 7

fact = 1
while n > 0:
    fact = fact * n
    n -= 1

print(fact)

# recursion class
def factorial(n):
    if n < 1 :
        return 1
    else:
        number = n * factorial(n-1)
        return number

print(factorial(7))

# Fibonnaci non recursive
def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

# Fibonacci recursive - be careful using recursion it can use a lot of resource if you use a big number.
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


print(fibonacci(30))
print(fibonacci2(30))