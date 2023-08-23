def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        buckets = [0] * 10
        
        for num in arr:
            digit = (num // exp) % 10
            buckets[digit] += 1
        
        for i in range(1, 10):
            buckets[i] += buckets[i - 1]
        
        sorted_arr = [0] * len(arr)
        
        for num in reversed(arr):
            digit = (num // exp) % 10
            buckets[digit] -= 1
            index = buckets[digit]
            sorted_arr[index] = num
        
        arr = sorted_arr
        exp *= 10
    
    return arr

arr = [123, 456, 789, 12, 34, 56]
sorted_arr = radix_sort(arr)
print(sorted_arr)