numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4

def search(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start <= end:  
        mid = (start + end) // 2  
        if numbers[mid] == target:
            print(f"Found target {target} at index {mid}")
            return mid  
        elif numbers[mid] > target:
            end = mid - 1  
        else:
            start = mid + 1  

    print(f"Target {target} not found")
    return -1  

search(numbers, target)
