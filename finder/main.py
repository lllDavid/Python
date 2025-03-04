usernames = ["david", "d_avid", "d.avid", "d_a_v_i_d", "d.w", "d.av.id", "w.david", "d_w"]

patterns = ["-", "_", "."]

results = []

for i in usernames:
    for j in patterns:
        if j in i:
            results.append(i)

print(results)



