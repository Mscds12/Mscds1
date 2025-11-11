def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)  # Output: Sorted array: [1, 2, 3, 4, 5, 6, 7, 8, 9]