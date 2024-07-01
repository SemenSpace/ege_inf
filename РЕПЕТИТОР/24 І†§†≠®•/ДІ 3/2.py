"""Текстовый файл 24-s1.txt состоит не более чем из 106 заглавных латинских букв (A..Z).
Текст разбит на строки различной длины.
Определите количество строк, в которых встречается комбинация Z*RO,
где звёздочка обозначает любой символ"""

f = open('2.txt')
f = [str(i)[:-1] for i in f]

alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'

count = 0
for i in f:
    for j in alph:
        if str(f'Z{j}RO') in i:
            count += 1
            break

print(count)