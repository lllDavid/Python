def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    diff = []
    
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append((s1[i], s2[i]))

    if len(diff) == 2:
        return diff[0] == diff[1][::-1]  

    return False

def areAlmostEqual2( s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    
    diff = []

    for char1, char2 in zip(s1, s2):
        if char1 != char2:
            diff.append((char1, char2))

    if len(diff) == 2:
        return diff[0] == diff[1][::-1]  

    return False

def areAlmostEqual3(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    
    setA = set()
    setB = set()
    
    for i,j in zip(s1,s2):
        if i != j:
            setA.update(i)
            setB.update(j)
    
    if len(setA) == 2 and len(setB) == 2:
        return setA == setB

    return False

print(areAlmostEqual("bank","bazk"))
print(areAlmostEqual2("bank","kanb"))
print(areAlmostEqual3("bank","kand"))