"""
Array -
linear data structure
contiguous memory allocation
access elements using index
homogeneous data type
use for -
suitable for storing and manipulating large amounts of data
efficient access and retrieval of elements
supports various operations like insertion, deletion, searching, sorting
"""
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
import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("The newly created array is: ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print("\r")
print("The index of the first occurrence of 2 is: ", end="")
print(arr.index(2))
print("The index of the first occurrence of 1 is: ", end="")
print(arr.index(1))