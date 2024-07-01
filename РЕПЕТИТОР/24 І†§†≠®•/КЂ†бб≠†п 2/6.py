f = open("24.1.txt")
f = f.readline()

f = f.replace("Y", "Y ")
f = f.replace("X", "X ")
f = f.split()

m = 0
for i in range(len(f) - 2):
    if f[i][-1] == f[i + 1][-1]:
        m = max(m, len(f[i]) + len(f[i + 1][:-1]))
    else:
        m = max(m, len(f[i]) + len(f[i + 1]) + len(f[i + 2][:-1]))

print(m)