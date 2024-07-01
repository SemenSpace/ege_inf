f = open("4.txt").readline().replace("XY", "*").replace("XZ", "*")

k = 0
mx = 0
for i in range(len(f)):
    if f[i] != "*":
        k += 1
    if f[i] == "*" and i != (len(f) - 1):
        mx = max(mx, k + 1)
        k = 1
    if i == (len(f) - 1):
        mx = max(mx, k)

print(mx)
