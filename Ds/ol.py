def ordered_linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return -1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = ordered_linear_search(arr, 5)
print("Element found at index:", index)  # Output: Element found at index: 4