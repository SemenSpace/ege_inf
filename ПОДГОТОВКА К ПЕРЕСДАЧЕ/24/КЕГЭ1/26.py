f = open("26.txt").readline()

f = f.replace("DBAC", "*")
mx = 0
k = 0
for i in range(len(f) - 3):
    if f[i] == "*":
        if f[i + 1] + f[i + 2] + f[i + 3] == "DBA":
            k += 7
            mx = max(mx, k)
            k = 0
        elif f[i + 1] + f[i + 2] == "DB":
            k += 6
            mx = max(mx, k)
            k = 0
        elif f[i + 1] == "D":
            k += 5
            mx = max(mx, k)
            k = 0
        else:
            k += 4
    if f[i] != "*":
        mx = max(mx, k)
        k = 0
print(mx)
