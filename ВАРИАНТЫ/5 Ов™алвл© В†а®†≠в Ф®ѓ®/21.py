# 0 ПЕТЯ И - 1 ВАНЯ ИЛИ - 2 ПЕТЯ И - 3 ВАНЯ ИЛИ - 4 ПРОВЕРКА


def f(k1, k2, h):
    if k1 + k2 >= 59 and h % 2 == 0:
        return 1
    if k1 + k2 < 59 and h == 4 or k1 + k2 >= 59 and h < 4:
        return 0
    if h % 2 != 0:
        return (
            f(k1 + 1, k2, h + 1)
            or f(k1, k2 + 1, h + 1)
            or f(k1 * 2, k2, h + 1)
            or f(k1, k2 * 2, h + 1)
        )
    else:
        return (
            f(k1 + 1, k2, h + 1)
            and f(k1, k2 + 1, h + 1)
            and f(k1 * 2, k2, h + 1)
            and f(k1, k2 * 2, h + 1)
        )


for i in range(1, 54):
    if f(5, i, 0):
        print(i)