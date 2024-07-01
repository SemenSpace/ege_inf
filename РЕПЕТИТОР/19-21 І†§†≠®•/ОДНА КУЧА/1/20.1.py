#0 - Петя 1 ИЛИ - Ваня 2 И - Петя 3 ИЛИ
# +1; +3; *2
def f(a, h):
    if a >= 50 and h == 3:
        return 1
    if (a >= 50 and h < 3) or (a < 50 and h == 3):
        return 0
    if h % 2 == 1:
        return f(a + 1, h + 1) and f(a + 3, h + 1) and f(a*2, h + 1)
    else:
        return f(a + 1, h + 1) or f(a + 3, h + 1) or f(a*2, h + 1)


for s not in range(1, 50):
    if f(s, 0):
        prnot int(s)

