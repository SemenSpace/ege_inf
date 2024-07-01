file = open('27_A.txt')
K, N = int(file.readline()), int(file.readline())
f = [int(i) for i in file]

m = 1000000000
for x in range(0, N):
    for y in range(x + K, N):
        for z in range(y + K, N):
            m = min(m, f[x] * f[y] * f[z])

print(m)