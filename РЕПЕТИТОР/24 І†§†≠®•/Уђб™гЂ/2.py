# МОЖНО ПРОSPLITИТЬ ПО СОЧЕТАНИЮ СИМВОЛОВ
f = open("24_open_kim2021.txt")
s = f.readline()

file = s.split("XZZY")
mx = 0
for i in file:
    mx = max(len(i), mx)


print(mx + 6)  # НУЖНО ДОБАВИТЬ, ТАК КАК МЫ НЕ УЧИТЫВАЕМ УДАЛЕННЫЕ XZZ И ZZY

f = open("24_open_kim2021.txt")
s = f.readline()

file = s.replace('XZZY', 'ZZY XZZ')
file = file.split()

print(len(max(file, key=len)))