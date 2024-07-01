f = open('2.txt')
d, e, n = map(int, f.readline().split())
f = [int(i) for i in f]

D = []
E = []
k = 0

# больше 500 мб записываются на D, остальные на E

for i in f:
    if i > 500:
        D.append(i)
    else:
        E.append(i)

last_D = 0
for i in sorted(D):
    if d - i > 0:
        k += 1
        d -= i
        last_D = i
    else:
        break

last_E = 0
for i in sorted(E):
    if e - i > 0:
        k += 1
        e -= i
        last_E = i
    else:
        break

print('', last_E, '-', e, '\n', last_D, '-', d)

e += last_E
d += last_D

mx_E = 0
mx_D = 0
for i in E:
    if i <= e:
        mx_E = max(i, mx_E)
for i in D:
    if i <= d:
        mx_D = max(i, mx_D)

print(k, mx_D + mx_E)


