def areAlmostEqual2(s1: str, s2: str) -> bool:
    diff = []
    if s1 == s2:
        return True

    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            diff.append((char1, char2))

    
    if len(diff) == 2:
        return diff[0] == diff[1][::-1]  

    return False

areAlmostEqual2("bank","kanb")