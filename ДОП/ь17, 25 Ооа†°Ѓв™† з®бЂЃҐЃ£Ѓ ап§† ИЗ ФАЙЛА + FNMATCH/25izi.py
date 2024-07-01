from fnmatch import *

# задание 25
# fnmatch(первый аргумент - само проверяемое число в str, второй - наша исходная маска)
# 37*87?
# * - many numbers
# ? - only one num

for x in range(1, 1000000, 1):
    if str(x)[:2] == '37' and str(x)[-3:-1] == '87' and x % 103 == 0:
        print(x, x // 103)

for x in range(103, 1000000, 103):  # <-- проходим по списку с шагом 103, т.к. от нас требуют числа делящиеся на 103
    if fnmatch(str(x), "37*87?"):
        print(x, x // 103)
