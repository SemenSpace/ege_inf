# 0 Петя И - 1 Ваня ИЛИ - 2 Петя И - 3 Ваня ИЛИ - 4 ПРОВЕРКА

def f(x, y, h):
    if x + y >= 47 and h == 4:
        return 1
    if (x + y >= 47 and h < 4) or (x + y < 47 and h == 4):
        return 0
    if h % 2 != 0:
        if max(x, y) > min(x, y):
            return (
                f(max(x, y) + 1, min(x, y), h + 1)
                or f(max(x, y) + 2, min(x, y), h + 1)
                or f(max(x, y) + 3, min(x, y), h + 1)
                or f(max(x, y), min(x, y) * 2, h + 1)
            )
        else:
            return (
                f(max(x, y) + 1, min(x, y), h + 1)
                or f(max(x, y) + 2, min(x, y), h + 1)
                or f(max(x, y) + 3, min(x, y), h + 1)
            )
    else:
        if max(x, y) > min(x, y):
            return (
                f(max(x, y) + 1, min(x, y), h + 1)
                and f(max(x, y) + 2, min(x, y), h + 1)
                and f(max(x, y) + 3, min(x, y), h + 1)
                and f(max(x, y), min(x, y) * 2, h + 1)
            )
        else:
            return (
                f(max(x, y) + 1, min(x, y), h + 1)
                and f(max(x, y) + 2, min(x, y), h + 1)
                and f(max(x, y) + 3, min(x, y), h + 1)
            )

kon = []



for i in range(1, 25):
    if f(22, i, 0):
        kon.append(i)
print(kon)

print(f(22, 2, 0))