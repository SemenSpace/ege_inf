f = open('27_A_2.txt')
n = int(f.readline())
f = [int(i) for i in f]


max = []
s = 0
ln = 0
for i in range(n):
    s += f[i]
    ln += 1
    if s % 43 != 0:
        max.append([s - f[i], ln - 1])
        s = f[i]
        ln = 1


max.sort(reverse=True)
print(max)