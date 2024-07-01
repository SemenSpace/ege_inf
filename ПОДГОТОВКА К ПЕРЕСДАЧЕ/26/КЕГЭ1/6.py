f = open('6.txt')
s, n = map(int, f.readline().split())
f = [int(i) for i in f]

k = 0

inc = []
all_ost = []
rare = []
for i in f:
    if i > 3000:
        rare.append(i)
    if 2000 <= i <= 3000:
        inc.append(i)
    if i < 2000:
        all_ost.append(i)

rare_mx = max(rare)
rare_mn = min(rare)

s = s - rare_mn - rare_mx
k += 2

for i in inc:
    k += 1
    s -= i

last = 0
ost = 0
for i in sorted(all_ost):
    if s - i >= 0:
        k += 1
        s -= i
        last = i
    else:
        ost = last + s
        break

mx = 0
for i in sorted(f):
    if i <= ost:
        mx = max(mx, i)
print(k, mx)