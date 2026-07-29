# Merging Dictionaries in Python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Method 1: Using the update() method
dict1.update(dict2)
print("Merged dictionary using update():", dict1)

# ** Method 2: Using the ** operator (Python 3.5+) **
dict3 = {**dict1, **dict2}
print("Merged dictionary using ** operator:", dict3)

# Method 3 only in Python 3.9+: Using the union operator (|)
dict4 = dict1 | dict2
print("Merged dictionary using union operator (|):", dict4)

# similar to above
dict3 = dict(dict1.items() | dict2.items())
print("Merged dictionary using items() and union:", dict3)