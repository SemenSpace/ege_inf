f = open('24.txt')
f = f.readline()

m = 0
k = 1
for i in range(1, len(f)):
    if f[i] != f[i - 1]:
        k += 1
    else:
        m = max(m, k)
        k = 1

print(m)
