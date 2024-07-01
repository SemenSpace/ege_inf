f = open('8.txt')
f = [int(i) for i in f]

count, mx = 0, 0

min_19 = 0
for i in sorted(f):
    if i % 19 == 0:
        min_19 = i
        break

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]

    if s1 % min_19 == 0 or s2 % min_19 == 0:
        count += 1
        mx = max(mx, s1 + s2)

print(count, mx)