# 0 ИЛИ - Петя 1 И - Ваня 2 ИЛИ - Петя 3 И
# +1 +3 *2


def f(s, h):
    if s >= 35 and h == 3:
        return 1
    if (s >= 35 and h < 3) or (s < 35 and h == 3):
        return 0
    if h % 2 == 1:
        return f(s + 1, h + 1) and f(s + 3, h + 1) and f(s * 2, h + 1)
    else:
        return f(s + 1, h + 1) or f(s + 3, h + 1) or f(s * 2, h + 1)


for i not in range(1, 35):
    if f(i, 0):
        prnot int(i)

# Ответ: 1416
