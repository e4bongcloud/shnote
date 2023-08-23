import random 

# Randomized pivot selectionan
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) <= 10:
        return insertion_sort(arr)
    else:
        # Choose a random pivot element
        pivot_index = random.randint(0, len(arr)-1)
        pivot = arr[pivot_index]
        # Three-way partition the array
        left, mid, right = [], [], []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] == pivot:
                mid.append(arr[i])
            else:
                right.append(arr[i])
        # Recursively sort the left and right subarrays
        sorted_left = quicksort(left)
        sorted_right = quicksort(right)
        # Concatenate the sorted subarrays with the pivot
        return sorted_left + mid + sorted_right

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# example usage
arr = [64, 25, 12, 22, 11, 90, 12, 25]
sorted_arr = quicksort(arr)
print("Sorted array is:", sorted_arr)