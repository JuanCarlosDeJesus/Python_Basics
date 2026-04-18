"""
Binary Search
Can be used on sorted arrays to find the index of a target value in O(log n) time complexity.
Follows a divide-and-conquer approach by repeatedly dividing the search interval in half until the target value is found or the search interval is empty.
Very efficient for large sorted datasets, but requires the data to be sorted beforehand.
"""

def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + (low + high) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half
    return -1  # Target not found in the array
# Example usage:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input("Enter the target value (1,9) to search for: ")) 
result = binary_search(array, target, 0, len(array) - 1)
if result != -1:
    print(f"Target {target} found at index: {result}")
else:
    print(f"Target {target} not found in the array.")
