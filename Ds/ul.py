def unordered_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [5, 2, 8, 1, 9, 3, 7, 4, 6]
index = unordered_linear_search(arr, 5)
print("Element found at index:", index)  # Output: Element found at index: 0