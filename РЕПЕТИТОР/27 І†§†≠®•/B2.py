f = open('test.txt')
n = int(f.readline())
a = [int(i) for i in f]

# 27-A_1 (1).txt
res = -10**10

for i in range(1, n - 1):

    ai = max(a[:i])
    aj = a[i]
    ak = max(a[i + 1:])

    if ai > aj and ak > aj:
        res = max(res, (ai + ak - (2 * aj)))
        print(a[:i], a[i], a[i + 1:])

print(res)