file = open('27A.txt')
n, k = int(file.readline()), int(file.readline())
f = [int(i) for i in file]
mn = 100000000
for x in range(n - 2*k):
    for y in range(x + 1, x + k):
        for z in range(y + 1, y + k):
            mn = min(mn, int(f[x]) * int(f[y]) * int(f[z]))

print(mn)

