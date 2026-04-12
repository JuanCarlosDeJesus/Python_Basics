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

