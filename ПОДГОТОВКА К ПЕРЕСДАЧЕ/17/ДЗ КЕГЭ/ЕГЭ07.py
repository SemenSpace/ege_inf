f = open('ЕГЭ07.txt')
f = [int(i) for i in f]

count = 0
mn = 10**10

min_el = min(f)
for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if (s1 % 55) == min_el or (s2 % 55) == min_el:
        count += 1
        mn = min(mn, s1 + s2)

print(count, mn)