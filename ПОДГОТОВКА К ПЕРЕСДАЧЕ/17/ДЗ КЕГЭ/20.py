f = open('20.txt')
f = [int(i) for i in f]

count = 0
mn = 10**10

summa = 0
for i in f:
    if i % 35 == 0:
        for j in str(i):
            summa += int(j)


for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]

    if s1 > summa and s2 <= summa and str(hex(s2))[-2:] == 'ef'\
            or s2 > summa and s1 <= summa and str(hex(s1))[-2:] == 'ef':
        count += 1
        mn = min(mn, s1+s2)

print(count, mn)
