# 0 - Петя 1 ИЛИ - Ваня 2 И - Петя 3 ИЛИ
# +1 +4 *5

def f(s, h):
    if s >= 68 and h == 3:
        return 1
    if (s >= 68 and h < 3) or (s < 68 and h == 3):
        return 0
    if h % 2 == 1:
        return f(s + 1, h +  1) and f(s + 4, h +  1) and f(s * 5, h +  1)
    else:
        return f(s + 1, h +  1) or f(s + 4, h +  1) or f(s * 5, h +  1)


for i in range(1, 70):
    if f(i, 0):
        print(i)