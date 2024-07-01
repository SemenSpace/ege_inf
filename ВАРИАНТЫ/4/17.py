f = open('17.txt')
f = [int(i) for i in f]
n = len(f)

m = 0
for i in sorted(f):
    if str(i)[-2:] == '12':
        m = max(m, i**2)

maxx = 0
count = 0
for x in range(n - 1):
    y = x + 1
    if ((str(f[x])[-2:] == '12' and str(f[y])[-2:] != '12')
        or (str(f[x])[-2:] != '12' and str(f[y])[-2:] == '12'))\
            and (f[x] + f[y]) ** 2 < m:
        count += 1
        maxx = max(maxx, f[x] + f[y])


print(count, maxx)