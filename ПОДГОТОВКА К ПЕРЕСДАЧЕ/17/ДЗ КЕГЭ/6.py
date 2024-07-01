f = open('6.txt')
f = [int(i) for i in f]

count = 0
mx = 0

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    su = s1 + s2
    if su % 3 == 0 and su % 6 != 0:
        if str(s1 * s2)[-1] == '8':
            count += 1
            mx = max(mx, su)

print(count, mx)