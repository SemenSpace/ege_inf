f = open('24.txt')
f = f.readline()

kol = dict()
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in alph:
    kol[i] = 0

for i in range(0, len(f) - 1):
    if f[i] == 'E':
        kol[f[i + 1]] += 1

m = 0
max_liter = ''
for i in alph:
    if kol[i] > m:
        m = kol[i]
        max_liter = i

print(m, max_liter)