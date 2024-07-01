f = open("27_A.txt")
n = int(f.readline())
f = [int(i) for i in f]

summa = 10**20

k = 0
for i in range(n):
    summa_0 = 0
    i += 1
    if i == 1:
        new1 = f[: n // 2 + i - 1]
        new2 = f[n // 2 + i - 1 :]
        new2.reverse()

    elif i <= n // 2 + 1:
        new1 = f[i - 1 : n // 2 + i - 1]
        s1 = f[n // 2 + i - 1 :]
        s2 = f[: i - 1]
        s1.reverse()
        s2.reverse()
        new2 = s2 + s1

    elif i > n // 2 + 1:
        new1 = f[i - 1:i + n // 2  - 1] + f[:i - n//2 - 1]
        new2 = f[i - n//2 - 1:i-1]
        new2.reverse()

    for x in range(len(new1)):
        summa_0 += new1[x]*x
    for x in range(len(new2)):
        summa_0 += new2[x]*(x+1)

    summa = min(summa, summa_0*3)

print(summa)
