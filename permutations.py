def permutations(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for p in permutations(rest):
            result.append([arr[i]] + p)
    return result

items = [1, 2, 3]
for p in permutations(items):
    print(p)