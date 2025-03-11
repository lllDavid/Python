def ulam_sequence(n):
    if n < 1:
        return []
    
    ulam = [1, 2]  
    while len(ulam) < n:
        next_candidate = ulam[-1] + 1
        while True:
            count = sum((next_candidate - u) in ulam for u in ulam if u < next_candidate)
            if count == 1:  
                ulam.append(next_candidate)
                break
            next_candidate += 1
    return ulam

print(ulam_sequence(10))
