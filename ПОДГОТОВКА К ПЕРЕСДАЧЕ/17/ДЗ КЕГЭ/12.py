f = open('12.txt')
f = [int(i) for i in f]
count = 0
mx = -10**10

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]

    su = s1 + s2
    if (s1 < 0 or s2 < 0) and su >= 100:
        count += 1
        mx = max(mx, s1 * s2)


print(count, mx)