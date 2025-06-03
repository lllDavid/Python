def compare_versions(v1, v2):
    parts1 = [int(x) for x in v1.split('.')]
    parts2 = [int(x) for x in v2.split('.')]

    length = max(len(parts1), len(parts2))
    parts1 += [0] * (length - len(parts1))
    parts2 += [0] * (length - len(parts2))
    return (parts1 > parts2) - (parts1 < parts2)  

print(compare_versions("1.2", "1.2.0"))  
print(compare_versions("1.2.1", "1.2.0"))  
print(compare_versions("1.1.9", "1.2"))  
