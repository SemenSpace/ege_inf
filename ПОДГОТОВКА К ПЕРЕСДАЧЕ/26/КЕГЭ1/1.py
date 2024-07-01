f = open('1.txt')
s, n = map(int, f.readline().split())
f = [int(i) for i in f]

f_naib = sorted(f, reverse=True)
s_naib = s
ostat = 0
k = 0
naim = 10**10

for i in f_naib:
    if s_naib - i > 0:
        s_naib -= i
        k += 1
    else:
        ostat = s_naib
        break
print(k, ostat)
