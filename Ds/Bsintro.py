def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        index = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[index] == target:
            return index
        elif arr[index] < target:
            low = index + 1
        else:
            high = index - 1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = interpolation_search(arr, 5)
print("Element found at index:", index)  # Output: Element found at index: 4