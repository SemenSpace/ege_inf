# 0 ПЕТЯ ИЛИ - 1 ВАНЯ ИЛИ - 2 ФИКСИРУЕМ ПРИБЫЛЬ
def f(k1, k2, h):
    if k1 + k2 >= 74 and h == 2:
        return 1
    if k1 + k2 >= 74 and h < 2 or k1 + k2 < 74 and h == 2:
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
            or f(k1, k2 + 1, h + 1)
            or f(k1 * 2, k2, h + 1)
            or f(k1, k2 * 2, h + 1)
        )


for i in range(1, 62):
    if f(12, i, 0):
        print(i)