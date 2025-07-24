def two_sum_sorted(nums, target):
    sorted_nums = sorted((n, i) for i, n in enumerate(nums))
    l, r = 0, len(nums) - 1
    while l < r:
        total = sorted_nums[l][0] + sorted_nums[r][0]
        if total == target:
            return [sorted_nums[l][1], sorted_nums[r][1]]
        elif total < target:
            l += 1
        else:
            r -= 1

from itertools import combinations

def two_sum_combinations(nums, target):
    for i, j in combinations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            return [i, j]



def optimized_cpu(current):
    next_target = ((current // 11) + 1) * 11
    if next_target > 100:
        next_target = 100
    say_count = next_target - current
    if say_count < 1 or say_count > 10:
        say_count = 1
    return say_count

def play():
    current = 0
    
    while current < 100:
        while True:
            try:
                user_say = int(input(f"Current count is {current}. How many numbers will you say? (1 to 10): "))
                if 1 <= user_say <= 10 and current + user_say <= 100:
                    break
                else:
                    print("Invalid number. Must be 1 to 10 and not exceed 100.")
            except ValueError:
                print("Enter a valid integer.")
        
        current += user_say
        print(f"You said numbers up to {current}")
        
        if current == 100:
            print("You said 100. You lose.")
            break
        
        cpu_say = optimized_cpu(current)
        current += cpu_say
        print(f"CPU says numbers up to {current}")
        
        if current == 100:
            print("CPU said 100. CPU loses. You win.")
            break

play()