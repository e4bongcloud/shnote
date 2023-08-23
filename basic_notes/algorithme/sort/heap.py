def heap_sort(arr):
    n = len(arr)
    
    # Build a max heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the heap in sorted order
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Find the largest element among i, left, and right
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If i is not the largest element, swap it with the largest element and heapify the subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

arr = [64, 25, 12, 22, 11]
sorted_arr = heap_sort(arr)
print("Sorted array is:", sorted_arr)