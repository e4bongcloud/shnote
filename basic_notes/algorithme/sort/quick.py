
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

# example usage
arr = [64, 25, 12, 22, 11, 90]
sorted_arr = quicksort(arr)
print("Sorted array is:", sorted_arr)