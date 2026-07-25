# Reverse List

# manual way
values = [1, 2, 3, 4, 5]

revlist = []
for i in range(len(values)):
    revlist.append(values[len(values) - 1 - i])
print(revlist)

# reverse() method
values = [1, 2, 3, 4, 5]

values.reverse()
print(values)

# reversed() method. will not overwrite the original list
values = [1, 2, 3, 4, 5]
revlist = list(reversed(values))
print(revlist)

# slicing method
values = [1, 2, 3, 4, 5]    
revlist = values[::-1]
print(revlist)