"""
Quick Sort
Divide and Conquer Algorithm
Recursive - every recursive call, a pivot is chosen and the array is partitioned into two 
sub-arrays, one with elements less than the pivot and one with elements greater than the pivot. 
The process is repeated on each sub-array until the base case of an array with 0 or 1 element 
is reached, which is inherently sorted.
So each step, array i reduced by 2 and the depth of the recursion is log(n) and each step we 
do n comparisons, so the time complexity is O(n log n)
Partition of elements take n time and problem is divided by half
best time complexity: O(n log n) - when the pivot divides the array into two equal halves
worst time complexity: O(n^2) - when the smallest or largest element is always
average time complexity: O(n log n) - when the pivot is reasonably well-chosen
Space complexity: O(log n) - due to recursive stack space in the best and average cases
Analysis:
Can be unstable - does not preserve the relative order of equal elements
In-place - does not require additional storage space for another array
"""
def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1  # Increment the pointer for the smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i + 1
    return i + 1  # Return the partitioning index

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partitioning index

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5, 3, 2, 4, 6]
print("Original array:", arr)
size = len(arr)
quick_sort(arr, 0, size - 1)
print("Sorted array:", arr)