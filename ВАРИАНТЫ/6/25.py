def delitel(n):
    k = 0
    ret = [1, n]
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            k += 1
            ret.append(i)
    if k == 2:
        return ret
    return []

kon = []
for i in range(201455, 201471):
    F = delitel(i)
    if len(F) == 4:
        kon.append(F)

for i in kon:
    i.sort()
    print(i[0], i[1], i[2], i[3])
