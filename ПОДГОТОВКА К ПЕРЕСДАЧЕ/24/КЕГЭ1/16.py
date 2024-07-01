f = open("16.txt").readline()

"""f = 'ASDPCCSGOPCNGCHPCPCSGOPC'"""

f = f.replace("CSGO", "**").replace("PC", "*")

k = 0
mx = 0
for i in range(len(f)):
    if f[i] == "*":
        k += 2
    if f[i] != "*":
        mx = max(mx, k)
        k = 0
    if f[i] == "*" and i == (len(f) - 1):
        mx = max(mx, k)

print(mx)


