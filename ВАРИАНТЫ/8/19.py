def f(k1, k2, h):
    if k1 + k2 >= 59 and h == 2:
        return 1
    if k1 + k2 >= 59 and h != 2 or k1 + k2 < 59 and h == 2:
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

for s in range(1, 54):
    if f(5, s, 0):
        print(s)