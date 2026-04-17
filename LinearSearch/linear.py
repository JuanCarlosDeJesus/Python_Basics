"""
Linear Search
Time Complexity: O(n)
Space Complexity: O(1) - no auxiliary data structures used
Search for an element in a linear manner. If the element is found, return the index of the element. Otherwise, return -1.
"""

def linear_search(arr, target, start=0):
    for i in range(start, len(arr)):
        if arr[i] == target:
            return i
    return -1


array = [1, 2, 3, 4, 5]
target = 3
result = linear_search(array, target)
if result == -1:
    print(f"{target} not found in the array.")
else:
    print(f"{target} found at index {result}.")