"""В текстовом файле 2.txt находится цепочка из символов
латинского алфавита A, B, C, D, E, F.
Найдите максимальную длину цепочки вида DBACDBACDBAC....
(состоящей из фрагментов DBAC,
последний фрагмент может быть неполным)."""

file = open('2.txt')
f = file.readline()

f = f.replace('E', 'F')


f = f.replace('DBAC', 'GGGG ')
f = f.replace(' DBA', 'GGG')
f = f.replace(' DB', 'GG')
f = f.replace(' D', 'G')

f = f.replace(' ', '')
print(f)
f = f.replace('A', 'F')
f = f.replace('B', 'F')
f = f.replace('C', 'F')
f = f.replace('D', 'F')

f = f.split('F')

m = 0
for i in f:
    m = max(i.count('G'), m)

print(m)

