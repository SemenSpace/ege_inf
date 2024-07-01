f = open("2.txt")
f = [int(i) for i in f]

count = 0
mn = 10**10

max_69 = 0
min_17 = 0

k = 0
for i in sorted(f):
    if i > 0 and i % 17 == 0:
        k += 1
        min_17 += i
    if k == 1 and i % 17 == 0:
        min_17 += i
        break

for i in sorted(f, reverse=True):
    if i % 100 == 69:
        max_69 = i**2

for i in range(len(f) - 3):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    s4 = f[i + 3]

    if (len(str(abs(s1))) == 3) + (len(str(abs(s2))) == 3) + (len(str(abs(s3))) == 3) + (len(str(abs(s4))) == 3) == 2:
        if (s1 % 18 == 0) + (s2 % 18 == 0) + (s3 % 18 == 0) + (s4 % 18 == 0) == 1:
            if (s1 + s2 + s3 + s4) % min_17 == 0:
                if s1 * s2 * s3 * s4 <= max_69:
                    count += 1
                    mn = min(mn, (s1 + s2 + s3 + s4)**2)

print(count, mn)