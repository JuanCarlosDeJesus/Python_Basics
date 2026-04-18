"""
Insertion Sort
Simple brute-force sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
Sort in accending order or decending order.
Maintains a sorted and unsorted part of the array. It iteratively takes an element from the unsorted part and inserts it into the correct position in the sorted part.
with every iteration, the sorted part grows by one element and the unsorted part shrinks by one element until the entire array is sorted.
First element is considered sorted, and the algorithm starts from the second element, comparing it with the elements in the sorted part and inserting it into the correct position. This process is repeated for all elements until the entire array is sorted.
We shift elements in the sorted part to the right to make space for the new element being inserted. This is done until we find the correct position for the new element.
continues until all elements are processed and the entire array is sorted.
"""
def insertion_sort(arr, order):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        if order == "asc":
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        else:
            while j >= 0 and key > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
order = input("Enter sorting order (asc/desc): ").lower()
ord = "Ascending" if order == "asc" else "Descending"
insertion_sort(arr, order)

print(f"Sorted {ord} array: {arr}")