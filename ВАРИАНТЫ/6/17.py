f = open('17.txt')
f = [int(i) for i in f]
m = 0
count = 0

for x in range(0, len(f) - 1):
    for y in range(x + 1, len(f)):
        s1 = f[x]
        s2 = f[y]
        s = s1 * s2
        if s % 26 == 0:
            count += 1
            m = max(m, s1 + s2)

print(count, m)


