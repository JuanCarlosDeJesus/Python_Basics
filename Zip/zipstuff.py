# Zip functions for the zipfile module.
names = ['Anna', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35, 40]

# using for
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old.")


print(list(zip(names, ages)))
# using zip
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")



# Zip used
sales = [100, 200, 300, 400]
costs = [50, 150, 250, 350]

for sale, cost in zip(sales, costs):
    profit = sale - cost
    print(f"Sale: {sale}, Cost: {cost}, Profit: {profit}")

# Unzipping
zipped = [('Anna', 25), ('Bob', 30), ('Charlie', 35), ('David', 40)]

names, ages = zip(*zipped)

print(list(names))  # Output: ['Anna', 'Bob', 'Charlie', 'David']
print(list(ages))   # Output: [25, 30, 35, 40]

# Using zip with 2 lists
letters = ['B', 'D', 'A', 'C']
numbers = [3, 2, 4, 1]

data = sorted(zip(letters, numbers))

print(data) # Output: [('A', 4), ('B', 3), ('C', 1), ('D', 2)]

# sorted numbers
data = sorted(zip(numbers, letters))

print(data) # Output: [(1, 'C'), (2, 'D'), (3, 'B'), (4, 'A')]

# Turning 2 list into a dictionary
letters = ['B', 'D', 'A', 'C']
numbers = [3, 2, 4, 1]

mydict = dict(zip(letters, numbers))
print(mydict) # Output: {'B': 3, 'D': 2