v1 = "1.23.2"
v2 = "1.25.8"

arrayV1 = list(map(int, v1.split(".")))
arrayV2 = list(map(int, v2.split(".")))

for i in range(min(len(arrayV1), len(arrayV2))):
    if arrayV1[i] > arrayV2[i]:
        print("Version1 newer")
        break
    elif arrayV1[i] < arrayV2[i]:
        print("Version2 newer")
        break
else:
    if len(arrayV1) > len(arrayV2):
        print("Version1 newer")
    elif len(arrayV1) < len(arrayV2):
        print("Version2 newer")
    else:
        print("Same versions")
