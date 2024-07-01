f = open('17.txt')
f = [int(i) for i in f]

max_238 = 0
for i in sorted(f, reverse=True):
    if str(i)[-3:] == '238':
        max_238 = i
        break

mx = 0
count = 0

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    five = 0
    krat_3 = 0
    krat_5 = 0
    summa = sum([s1, s2, s3])
    for j in [s1, s2, s3]:
        if len(str(j)) == 5:
            five += 1
        if j % 3 == 0:
            krat_3 += 1
        if j % 5 == 0:
            krat_5 += 1

    if five == 2 or five == 1:
        if krat_3 > krat_5:
            if summa > max_238:
                mx = max(mx, summa)
                count += 1

print(count, mx)

