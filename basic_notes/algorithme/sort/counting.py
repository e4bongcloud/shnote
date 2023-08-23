def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    sorted_arr = [0] * len(arr)

    # Count the occurrences of each value
    for val in arr:
        counts[val] += 1

    # Accumulate the counts to determine the position of each value in the sorted array
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    # Build the sorted array by iterating over the original array in reverse
    for val in reversed(arr):
        index = counts[val] - 1
        sorted_arr[index] = val
        counts[val] -= 1

    return sorted_arr

arr = [5, 2, 7, 3, 9, 4, 1, 6, 8]
sorted_arr = counting_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
