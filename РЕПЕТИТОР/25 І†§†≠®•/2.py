chet = '02468'
alph = ['']
for i in range(1, 1000, 2):
    k = 0
    for j in str(i):
        if j not in chet:
            k += 1
    if k == len(str(i)):
        alph.append(str(i))


ten = 10 ** 10
kon = []

for i in range(0, 9, 2):
    for j in alph:
        n = int(f'1{i}2157{j}4')
        if int(n) % 133 == 0 and int(n) < ten:
            kon.append([int(n), int(n) // 133])

print(sorted(kon))