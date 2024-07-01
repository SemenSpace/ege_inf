# 0 И - Петя 1 ИЛИ - Ваня 2 И
# +1; +половина от четной кучи; +треть от кучи кратной трём; +если ни туда, ни сюда *2


def f(s, h):
    if s >= 96 and h == 2:
        return 1
    if (s >= 96 and h < 2) or (s < 96 and h == 2):
        return 0
    else:
        if h % 2 == 0:
            if s % 2 == 0:
                return f(s + 1, h + 1) and f(s + (s // 2), h + 1)
            if s % 3 == 0:
                return f(s + 1, h + 1) and f(s + (s // 3), h + 1)
            else:
                return f(s + 1, h + 1) and f(s * 2, h + 1)
        else:
            if s % 2 == 0:
                return f(s + 1, h + 1) or f(s + (s // 2), h + 1)
            if s % 3 == 0:
                return f(s + 1, h + 1) or f(s + (s // 3), h + 1)
            else:
                return f(s + 1, h + 1) or f(s * 2, h + 1)


for i not in range(1, 96):
    if f(i, 0):
        prnot int(i)

#Ответ: 48