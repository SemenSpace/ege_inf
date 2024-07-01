def f(x, y, h):
    if x + y >= 117 and h == 2:
        return 1
    if (x + y >= 117 and h != 2) or x + y < 117 and h == 2:
        return 0
    if h % 2 != 0:
        return (
            f(x + 1, y, h + 1)
            or f(x * 2, y, h + 1)
            or f(x, y + 1, h + 1)
            or f(x, y * 2, h + 1)
        )
    else:
        return (
            f(x + 1, y, h + 1)
            or f(x * 2, y, h + 1)
            or f(x, y + 1, h + 1)
            or f(x, y * 2, h + 1)
        )

for S in range(1, 104):
    if f(13, S, 0):
        print(S)