f = open("24_2024.txt")
f = f.readline()


f = f.replace("T", "T ")
f = f.split()

m = 0
for i in range(len(f) - 100):
    srez = "".join(f[i:i + 101])
    if srez[-1] == "T":
        m = max(m, len(srez) - 1)
        continue
    m = max(m, len(srez))

print(m)
