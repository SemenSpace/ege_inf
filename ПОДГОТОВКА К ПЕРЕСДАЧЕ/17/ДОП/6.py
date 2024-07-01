f = open('6.txt')
f = [int(i) for i in f]

count = 0
mx = 0
sum_sr = 0
kol_sr = 0

for i in f:
    if i % 2 != 0:
        sum_sr += i
        kol_sr += 1

sr = sum_sr/kol_sr


for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if s1 % 5 == 0 or s2 % 5 == 0:
        if s1 < sr or s2 < sr:
            count += 1
            mx= max(mx, s1 + s2)

print(count, mx)
