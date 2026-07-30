# Value of List
mylist=[1,2,3,4,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,2,1,1,3,4,1,1,1,1,1,1,]

current_max = 0
current_val = None

for val in mylist:
    if mylist.count(val) > current_max:
        current_max = mylist.count(val)
        current_val = val

print(f"The most frequent value is {current_val} and it appears {current_max} times.")

# Using Counter from collections module
from collections import Counter

mylist=[1,2,3,4,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,2,1,1,3,4,1,1,1,1,1,1,]

# a list is created with the most common values and their counts
counter = Counter(mylist)
print(counter)  # Counter({1: 13, 2: 10, 3: 4, 4: 4})

# This prints the most common value and its count
most_common = counter.most_common(1)[0]  # {1: 13}
print(f"The most frequent value is {most_common[0]} and it appears {most_common[1]} times.")

# Using max() function with key argument
mylist=[1,2,3,4,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,2,1,1,3,4,1,1,1,1,1,1,]

# using max() on list gets you the highest value = 4 but key count() gets you = 1
print(max(mylist)) # 4
print(max(set(mylist), key=mylist.count))  # 1
print(mylist.count(max(set(mylist), key=mylist.count)))  # 13

print(f"The most frequent value is {max(set(mylist), key=mylist.count)} and it appears {mylist.count(max(set(mylist), key=mylist.count))} times.")
