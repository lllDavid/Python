from re import match
from functools import cmp_to_key

def parse_version(v):
    _match = match(r"^(\d+(?:\.\d+)*)(?:-([a-zA-Z0-9]+))?$", v)
    if not _match:
        raise ValueError(f"Invalid version format: {v}")
    main_version = [int(x) for x in _match.group(1).split('.')]
    prerelease = _match.group(2) or ""
    return main_version, prerelease

def compare_versions(v1, v2):
    parts1, pre1 = parse_version(v1)
    parts2, pre2 = parse_version(v2)

    length = max(len(parts1), len(parts2))
    parts1 += [0] * (length - len(parts1))
    parts2 += [0] * (length - len(parts2))

    if parts1 > parts2:
        return 1
    elif parts1 < parts2:
        return -1

    if pre1 == pre2:
        return 0
    elif not pre1:  
        return 1
    elif not pre2:
        return -1
    else:
        return (pre1 > pre2) - (pre1 < pre2)

print(compare_versions("1.2", "1.2.0"))         
print(compare_versions("1.2.1", "1.2.0"))       
print(compare_versions("1.1.9", "1.2"))         
print(compare_versions("1.2.0-alpha", "1.2.0")) 
print(compare_versions("1.2.0-beta", "1.2.0-alpha")) 

versions = ["1.2.0", "1.2.0-alpha", "1.1.9", "1.2", "1.2.1"]
versions.sort(key=cmp_to_key(compare_versions))
print(versions)