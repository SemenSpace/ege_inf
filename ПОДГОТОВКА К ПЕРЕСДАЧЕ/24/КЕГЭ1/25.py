f = open("25.txt").readline()


f = f.replace("CA", "*")
k = 0
mx = 0

for i in range(len(f) - 1):
    if f[i] == "*":
        if f[i + 1] == "C":
            k += 3
            mx = max(mx, k)
            k = 0
        else:
            k += 2
    if f[i] != "*":
        mx = max(mx, k)
        k = 0

print(mx)
