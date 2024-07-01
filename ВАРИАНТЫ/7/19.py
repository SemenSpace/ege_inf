def f(k, h):
    if k >= 361 and h == 2:
        return 1
    if k >= 361 and h != 2 or k < 361 and h == 2:
        return 0
    if h % 2 != 0:
        return f(k + 1, h + 1) or f(k * 6, h + 1)
    else:
        return f(k + 1, h + 1) or f(k * 6, h + 1)

for i in range(1, 361):
    if f(i, 0):
        print(i)
