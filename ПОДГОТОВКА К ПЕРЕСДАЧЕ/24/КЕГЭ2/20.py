f = open('20.txt')
f = [str(i) for i in f]

last = ''
kol_povtor = 0

for i in f:
    mx = 0
    k = 0
    for j in range(len(i) - 1):
        s1 = i[j]
        s2 = i[j + 1]
        if s1 == s2:
            k += 1
        else:
            mx = max(mx, k)
    if mx > kol_povtor:
        kol_povtor = mx
        last = i


c = 0
b = ''
for i in sorted(last):
    if last.count(i) > c:
        c = last.count(i)
        b = i

print(b, ''.join(f).count(b))