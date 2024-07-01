f = open('ЕГЭ08.txt')
f = [int(i) for i in f]
count = 0
mx = 0

kol_32 = 0
for i in f:
    if i % 32 == 0:
        kol_32+=1

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if s1 < 0 or s2 < 0:
        if s1 + s2 < kol_32:
            count += 1
            mx = max(mx, s1 + s2)

print(count, mx)