f = open("27.txt").readline()

f = f.replace("XYZ", "*")
k = 0
mx = 0
for i in range(2, len(f) - 2):
    print(k)
    if f[i] == "*":
        if f[i - 2 : i] == "YZ":
            k += 3 + 2
        elif f[i - 1] == "Z":
            k += 3 + 1
        elif f[i + 1 : i + 3] == "XY":
            k += 3 + 2
            mx = max(mx, k)
            k = 0
        elif f[i + 1] == "X":
            k += 3 + 1
            mx = max(mx, k)
            k = 0
        else:
            k += 3
    if f[i] != "*":
        mx = max(mx, k)
        k = 0

print(mx)
