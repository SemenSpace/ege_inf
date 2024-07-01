f = open('17.txt')
f = [int(i) for i in f]

m = 0
for i in sorted(f):
    if len(str(i)) == 2:
        m = max(m, i)

mx = 0
count = 0
for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if len(str(s1)) == 2 and len(str(s2)) != 2 or len(str(s2)) == 2 and len(str(s1)) != 2:
        summa = s1 + s2
        if summa % m == 0:
            count += 1
            mx = max(mx, summa)

print(count, mx)
