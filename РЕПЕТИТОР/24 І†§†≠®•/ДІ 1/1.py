"""В текстовом файле 1.txt находится цепочка
из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки,
не содержащей гласных букв."""


file = open('1.txt')
f = file.readline()
f = f.replace('A', 'E')
f = f.split('E')

m = 0
for i in f:
    m = max(m, len(i))

print(m)