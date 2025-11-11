def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)  # Output: Sorted array: [1, 2, 3, 4, 5, 6, 7, 8, 9]