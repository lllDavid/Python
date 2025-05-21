def quicksort(arr):
    if len(arr) <= 1:
        return arr  
    
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]      
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]     
    
    return quicksort(left) + middle + quicksort(right)

nums = [33, 10, 55, 71, 29, 3, 7]
sorted_nums = quicksort(nums)
print(sorted_nums)
