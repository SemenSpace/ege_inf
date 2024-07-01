f = open('27-A.txt')
n = int(f.readline())
f = [int(i) for i in f]

m = 0
for x in range(n - 2):
    for y in range(x + 1, n - 1):
        for z in range(y + 1, n):
            s = f[x] + f[y] + f[z]
            if s % 3 == 0:
                m = max(m, s)

print(m)