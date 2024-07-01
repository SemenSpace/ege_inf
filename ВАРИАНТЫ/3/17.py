file = open('17.txt')
f = [int(i) for i in file]


min_sqrt_na_6 = 0
for i in sorted(f):
    if str(i)[-1] == '6':
        min_sqrt_na_6 = i**2
        break

m = 0
count = 0
for i in range(len(f) - 1):
    x = f[i]
    y = f[i + 1]
    s = x**2 + y**2

    if (str(x)[-1] == '6' and  str(y)[-1] != '6') or (str(x)[-1] != '6' and  str(y)[-1] == '6'):
        if s < min_sqrt_na_6:
            count += 1
            m = max(m, s)

print(count, m)
