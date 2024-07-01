f = open('1.txt')
f = [int(i) for i in f]


min_el = 0
for i in sorted(f):
    if i % 19 == 0:
        min_el = i
        break

mx = 0
count = 0
for i in range(1, len(f)):
    if f[i] % min_el == 0 or f[i - 1] % min_el == 0:
        count += 1
        mx = max(mx, f[i]+f[i - 1])

print(count, mx)