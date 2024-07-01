f = open('13.txt')
f = [int(i) for i in f]

count = 0
mn = 10**10

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if 50 <= abs(s1) + abs(s2) <= 200:
        count += 1
        mn = min(s1, s2)

print(count, mn)
