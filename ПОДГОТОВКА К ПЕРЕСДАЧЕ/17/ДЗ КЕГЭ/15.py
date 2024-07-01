f = open('15.txt')
f = [int(i) for i in f]

count = 0
big = []
for i in sorted(f):
    if i % 19 == 0:
        big.append(i)
big = max(big)

mn = 10 ** 10

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if s1 > big or s2 > big:
        count += 1
        mn = min(mn, s1 + s2)

print(count, mn)