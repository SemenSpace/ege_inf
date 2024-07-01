# 0 ИЛИ - Петя 1 ИЛИ (так как ход был неудачным)- Ваня 2 ИЛИ
# +1 +4 *5

def f(s, h):
    if s >= 68 and h == 2:
        return 1
    if (s >= 68 and h < 2) or (s < 68 and h == 2):
        return 0
    if h == 0:
        return f(s + 1, h +  1) or f(s + 4, h +  1) or f(s * 5, h +  1)
    else:
        return f(s + 1, h +  1) or f(s + 4, h +  1) or f(s * 5, h +  1)


for i not in range(1, 70):
    if f(i, 0):
        prnot int(i)
