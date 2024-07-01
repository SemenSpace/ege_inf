f = open("6.txt").readline().replace("XZZY", "*")
print(f)
f = f.split("*")
mx = 0
for i in f:
    if i != f[0] and i != f[-1]:
        mx = max(mx, len(i) + 6)
    if i == f[0] or i == f[-1]:
        mx = max(mx, len(i) + 3)
