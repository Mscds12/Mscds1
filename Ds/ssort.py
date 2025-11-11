def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)  # Output: Sorted array: [1, 2, 3, 4, 5, 6, 7, 8, 9]