f = open('5.txt')
f = [int(i) for i in f]


count = 0
mx = 0

for i in range(len(f) - 2):
    a = f[i]
    b = f[i + 1]
    c = f[i + 2]
    ma = max(a, b, c)
    mi = min(a, b, c)
    sr = sum([a, b, c]) - ma - mi

    if ma ** 2 < sr ** 2 + mi ** 2:
        count += 1
        mx = max(mx, (a + b + c))

print(count, mx)

    