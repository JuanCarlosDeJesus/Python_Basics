"""
Merge Sort
Divide array into two halves, sort them recursively and then merge the sorted halves.
Efficiency: O(n log n) in all cases
Divide and Conquer 
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        y = z = d = 0
        while y < len(L) and z < len(R):
            if L[y] < R[z]:
                arr[d] = L[y]
                y += 1
            else:
                arr[d] = R[z]
                z += 1
            d += 1
        while y < len(L):
            arr[d] = L[y]
            y += 1
            d += 1
        while z < len(R):
            arr[d] = R[z]
            z += 1
            d += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver code to test the above
if __name__ == '__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Given array is", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)
    