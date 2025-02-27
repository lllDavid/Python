paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

def Solution(paths: list[list[str]]) -> str:
    outs = set()
    ins = set()

    for a,b in paths:
        outs.add(a)
        ins.add(b)

    return [b for b in ins if b not in outs][0]

print(Solution(paths))