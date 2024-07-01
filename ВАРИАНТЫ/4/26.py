f = open('26.txt')
n = int(f.readline())
f = sorted([int(i) for i in f])

print(f)
komplecti = []
for i in range(n - 1, 0, -1):
    kon = [f[i]]
    for j in range(i - 1, -1, -1):
        if kon[-1] - f[j] >= 6:
            kon.append(f[j])
        else:
            komplecti.append(kon)

komplecti = sorted(komplecti, reverse=True)
first = len(max(komplecti, key=len))

second = 0
for i in komplecti:
    if len(i) == first:
        second = max(second, i[-1])

print(first, second)

