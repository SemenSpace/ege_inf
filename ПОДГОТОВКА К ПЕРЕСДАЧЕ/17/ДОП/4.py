f = open('4.txt')
f = [int(i) for i in f]

count = 0
mx = 0

for x in range(len(f) - 1):
    for y in range(x + 1, len(f)):
        s1 = f[x]
        s2 = f[y]
        su = s1 + s2
        if su %  2 != 0:
            if (s1 * s2) % 3 == 0:
                count += 1
                mx = max(mx, su)

print(count, mx)
