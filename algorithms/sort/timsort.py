def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def timsort(arr):
    n = len(arr)
    MIN_RUN = 32  

    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min((i + MIN_RUN - 1), (n - 1)))

    size = MIN_RUN
    while size < n:
        for left in range(0, n, size * 2):
            mid = min((left + size - 1), (n - 1))
            right = min((left + size * 2 - 1), (n - 1))
            
            if mid < right:  
                merge(arr, left, mid, right)
        
        size *= 2

    return arr

if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6, 3, 8, 4, 7]
    print("Original array:", arr)
    
    sorted_arr = timsort(arr)
    print("Sorted array:", sorted_arr)

    import random
    large_arr = [random.randint(1, 1000) for _ in range(100)]
    print("\nLarge random array (first 10):", large_arr[:10])
    timsort(large_arr)
    print("Sorted large array (first 10):", large_arr[:10])