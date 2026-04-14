import array

"""
Array -
linear data structure
contiguous memory allocation
access elements using index
homogeneous data type
mutable (can be modified after creation)
use for -
suitable for storing and manipulating large amounts of data
efficient access and retrieval of elements
supports various operations like insertion, deletion, searching, sorting
"""

# Basic operations on arrays
# 1. Creation of an array
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates that the array will hold integers
print("The created array is: ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")
# 2. Accessing elements
print(arr[0]) # Accessing the first element           
# 3. Finding the length of the array using len() function
print("The length of the array is: ", end="")
print(len(arr))
# 4. Adding elements to the array using append() method
arr.append(6)
print("The array after appending 6 is: ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
# 5. Extending the array using extend() method
arr.extend([7, 8, 9])  # Extending the array with []
print("\nThe array after extending with [7, 8, 9] is: ", end="")
for i in range(0, 9):
    print(arr[i], end=" ")
# 6. Inserting an element at a specific index using insert() method
arr.insert(0, 0) # Inserting 0 at index 0
print("\nThe array after inserting 0 at index 0 is: ", end="")
for i in range(0, 10):
    print(arr[i], end=" ")
# 7. Removing an element using Pop() method and returning the removed element
arr.pop() # Removing the last element
print("\nThe array after popping the last element is: ", end="")
for i in range(0, 9):
    print(arr[i], end=" ")
arr.pop(0) # Removing the first element
print("\nThe array after popping the first element is: ", end="")
for i in range(0, 8):
    print(arr[i], end=" ")
# 8 Removing an element using remove() method. Remove value does not return the removed element
#   You must specify the value to remove, not the index. If the value is not found, it raises a ValueError.
arr.remove(0) # Removing the first occurrence of 0
print("\nThe array after removing 0 is: ", end="")
for i in range(0, 8):
    print(arr[i], end=" ")
# 9. Array Concatenation using + operator
arr1 = array.array('i', [1, 2, 3])
arr2 = array.array('i', [4, 5, 6])
arr3 = arr1 + arr2
print("\nThe concatenated array is: ", end="")
for i in range(0, 6):
    print(arr3[i], end=" ")
# 10. Array Slicing
print("\nThe sliced array from index 2 to 5 is: ", end="")
for i in range(2, 5):
    print(arr3[i], end=" ")
# 11. Printing the array in reverse order using slicing
print("\nThe array in reverse order is: ", end="")
for i in range(len(arr3)-1, -1, -1):
    print(arr3[i], end=" ")
print(arr3[::-1]) # Another way to print the array in reverse order using slicing - not recommended for large arrays as it creates a new array in memory
# 12. Looping through the array using for loop
print("\nLooping through the array using for loop: ", end="")
for i in range(0, len(arr3)):
    print(arr3[i], end=" ")
#13. Looping through the array using while loop. Using interator, condition, incrementation
print("\nLooping through the array using while loop: ", end="")
i = 0
while i < len(arr3):
    print(arr3[i], end=" ")
    i += 1


"""
1D array
can be a row
one index used
Declaration - and initialization of 1D array
  ex. int arr[5] or int arr[] = {1, 2, 3, 4, 5}
"""

print("How many elements do you want to store in the array?", end=" ")
num = input()
arr = []

for i in range(int(num)):
    print(f"Enter {num} elements:", end="")
    element = input()
    arr.append(element)
print("The array is:", arr)
for i in range(int(num)):
    print(f"Element at index {i} is: {arr[i]}")

"""  
2D array
can be a table
two indices used
"""
r_num = int(input("Enter the number of rows: "))
c_num = int(input("Enter the number of columns: "))
two_d_array = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        # print(f"Enter element for row {i} and column {col}:", end="")
        two_d_array[row][col] = row * col
print(f"The 2D array is: {two_d_array}")

"""
multi-dimensional array
can be a cube or higher-dimensional structure
multiple indices used
"""

# Delete elements from the array
print("Enter the size of the array:", end="")
tot = int(input())
arr = []
print(end=f"Enter {tot} elements: ")
for i in range(tot):
    arr.append(input())

print(end="\nEnter the value to delete: ")
val = input()

if val in arr:
    arr.remove(val)
    print("\nThe New Array is: ")
    for i in range(tot - 1):
        print(end=arr[i]+" ")
else:
    print("\nValue not found in the array.")


# Sort the array
arr = [10,22,38,27,11]
temp = 0

# Displaying the unsorted array
print("The unsorted array is: ", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
# Sorting the array in ascending order
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print()
# Displaying the sorted array
print("The sorted array is: ", end="")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# Search for an element in the array

arr = array.array('i', [1, 2, 3, 1, 2, 5])  # 'i' indicates that the array will hold integers
print("The newly created array is: ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print("\r")
print("The index of the first occurrence of 2 is: ", end="")
print(arr.index(2))
print("The index of the first occurrence of 1 is: ", end="")
print(arr.index(1))