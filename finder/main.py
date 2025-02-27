usernames = ["david", "d_avid", "d.avid", "d_a_v_i_d", "d.w", "d.wagner", "david.wagner", "d_wagner"]

patterns = ["-", "_", "."]

results = []

for i in usernames:
    for j in patterns:
        if j in i:
            results.append(i)

print(results)



