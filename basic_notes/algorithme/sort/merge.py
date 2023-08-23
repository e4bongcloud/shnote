def merge_sort(arr):
    # Base case: an empty or single-element array is already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two subarrays
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the left and right subarrays
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    # Merge the sorted subarrays
    merged = []
    i, j = 0, 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1
    merged += sorted_left[i:]
    merged += sorted_right[j:]
    
    return merged

arr = [64, 25, 12, 22, 11]
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)