def prostoe_li(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return 0
    return [diapozon.index(n) + 1, n]


diapozon = [i for i in range(245690, 245756 + 1)]

kon = []
for i in diapozon:
    kon.append(prostoe_li(i))

kon.remove(0)
print(kon)