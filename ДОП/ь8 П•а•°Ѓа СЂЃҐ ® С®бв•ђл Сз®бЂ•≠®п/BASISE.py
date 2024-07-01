from itertools import *

# product - генератор "слов" из заданного алфавита (его берем из задания)
# repeat - длина слова для PRODUCT

# permutations - генератор "слов" из заданного алфавита путем ПЕРЕСТАНОВКИ
# r - длина слова при PERMUTATIONS

numb = 1  # номер нашего слова в порядке возрастания из всех возможных вариантов
for i in product('АБВГДЕЖЗИК', repeat=3):  # генерирует все возможные варианты длиной (repeat) 3
    # print(numb, i) <- на выходе получается не список, а МНОЖЕСТВО/TUPLE

    if ''.join(i) == 'АГА':
        #     ''. <- разделитель
        print(''.join(i), numb)  # чтобы получить строчку просто склеиваем через ''.join(НАШ ТЬЮПАЛ КОРТЕЖ)

    numb += 1

"""ЗАДАЧА НА ПЕРЕСТАНОВКУ БУКВ (ОДИН РАЗ БУКВА В СЛОВЕ)"""

count = 0
for i in permutations('КАСПЕР', r=6):
    count += 1
print(count)

"""ЗАДАЧА С ПЕРЕВОДОМ В СИСТЕМУ СЧИСЛЕНИЯ"""
# from itertools import *
numb = 1

# АДИН - четверичная систему счисления
#                                 <- пятеричная система счисления
for i in product('АДИН', repeat=5):
    if ''.join(i) == 'ДИАНА':
        print(numb)
    numb += 1

"""ЗАДАЧА НА ПОИСК СЛОВА ПО ЕГО НОМЕРУ"""
# наше искомое слово находится под номером 1055,
# а это значит, что нам нужно перевести 1055 - 1
# в систему счисления нашего алфавита

# from itertools import *
count = 1
for i in product('EMNOY', repeat=5):
    if count == 1055:
        print(''.join(i))  # -> MONEY
    count += 1

# перевод числа из пятеричной в десятичную
n = 1055 - 1
kon = []
while n > 0:
    kon.append(n % 5)
    n //= 5
print(kon[::-1])  # -> [1 (M), 3 (O), 2 (N), 0 (E), 4 (Y)]

"""ЗАДАЧА НА НАХОЖДЕНИЕ КОЛИЧЕСТВА БУКВ В СЛОВАХ"""

# from itertools import *
count = 0
for i in product('LOST', repeat=7):
    if i.count('O') == 3:
        count += 1

print(count)

# from itertools import *
count = 0
for i in product('PLAN', repeat=6):
    if 4 >= i.count('A') > 0:
        count += 1

print(count)

# from itertools import *
count = 0
for i in product('QWER123', repeat=5):
    # проверка на то, что в нашем слове встречается ровно ДВЕ цифры
    if (i.count('1') + i.count('2') + i.count('3')) == 2:
        count += 1

print(count)

# from itertools import *
count = 0
for i in product('БАНДЕРОЛЬ', repeat=7):
    # проверка на то, что в нашем слове больше гласных, чем согласных
    # МЯГКИЙ ЗНАК НЕ СОГЛАСНАЯ И НЕ ГЛАСНАЯ
    sogl = 0
    gl = 0
    for j in i:
        if j in "БНДРЛ":
            sogl += 1
        if j in "АЕО":
            gl += 1
    if gl > sogl:
        count += 1

print(count)

# from itertools import *
count = 0
for i in product('012345678', repeat=6):
    # только одна цифра три и рядом только нечетные
    if i.count('3') == 1 and i[0] != '0':
        if (i.index('3') == 0) and (int(i[1]) % 2 != 0):
            count += 1
        if (5 > i.index('3') > 0) and (int(i[i.index('3') + 1]) % 2 != 0) and (int(i[i.index('3') - 1]) % 2 != 0):
            count += 1
        if (i.index('3') == 5) and (int(i[4]) % 2 != 0):
            count += 1
print(count)

# from itertools import *
count = 0
for i in product('01234567', repeat=5):
    # проверка на то, что в нашем слове ровно ДВЕ 5 и рядом с 2 не стоит нечетная цифра
    s = ''.join(i)
    if i.count('5') == 2 and i[0] != '0':
        if ('12' not in s and '21' not in s and
                '32' not in s and '23' not in s and
                '52' not in s and '25' not in s and
                '72' not in s and '27' not in s):
            count += 1

print(count)


"""ЗАДАЧА НА ПЕРЕСТАНОВКУ БУКВ (ОДИН РАЗ БУКВА В СЛОВЕ)"""

# from itertools import *
count = 0
for i in set(permutations('QWERTYU', r=5)):
    s = ''.join(i)
    if i[0] != 'W' and 'QE' not in s:
        count += 1
print(count)


"""ЗАДАЧА НЕ ПЕРЕСТАНОВКУ С ДВУМЯ ОДИНАКОВЫМИ БУКВАМИ"""

# ЕСЛИ НУЖНО БЕЗ ПОВТОРОВ, ТО ИСПОЛЬЗУЕМ SET (МНОЖЕСТВО)
count = 0
for i in set(permutations('КАРЕТА', r=4)):
    s = ''.join(i)
    if 'АА' not in s:
        count += 1
print(count)
