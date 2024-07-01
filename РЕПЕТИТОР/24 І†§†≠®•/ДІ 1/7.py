"""Текстовый файл 24-J5.txt состоит не более чем из 106 символов S, T, O, C, K.
Сколько раз встречается комбинация «OCK», не являющаяся при этом частью комбинации «STOCK»."""

f = open('7.txt')
f = f.readline()

f = f.replace('OCK', 'G')
f = f.replace('STG', 'X')

"""f = f.replace('S', 'X')
f = f.replace('T', 'X')
f = f.replace('O', 'X')
f = f.replace('C', 'X')
f = f.replace('K', 'X')"""

print(f.count('G'))


