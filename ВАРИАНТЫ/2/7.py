# 0 Петя - 1 Ваня - 2 Петя - 3 Ваня - 4
def f(n, h):
    if (n >= 68) and (h % 2 != 0):
        return 1
    if (n >= 68 and h < 4) or (n < 68 and h == 4):
        return 0
    if h == 1 or h == 3:
        return f(n + 1, h + 1) or f(n + 4, h + 1) or f(n * 5, h + 1)
    else:
        return f(n + 1, h + 1) and f(n + 4, h + 1) and f(n * 5, h + 1)


for i in range(1, 68):
    if f(i, 0):
        print(i)
