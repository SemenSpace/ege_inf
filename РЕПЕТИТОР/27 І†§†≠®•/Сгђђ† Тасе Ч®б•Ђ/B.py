file = open('27-B.txt')
n = int(file.readline())
f = [int(i) for i in file]

"""
остатки от деления на 3-и с 3-мя числами
0 0 0
0 1 2
1 1 1
2 2 2
в сумме эти остатки дают числа, которые делятся на 3
(поэтому тут нет комбинаций вроде 022 или 122)
"""

maxx = {i: [0] for i in range(3)}
for i in f:
    ost = i % 3
    if i > max(maxx[ost]):
        maxx[ost] += [i]
        if len(maxx[ost]) > 3:
            maxx[ost].remove(min(maxx[ost]))

m = 1
if len(maxx[0]) > 1 and len(maxx[1]) > 1 and len(maxx[2]) > 1:
    m = max(m, max(maxx[0]) + max(maxx[1]) + max(maxx[2]))
for i in range(3):
    if 1 not in maxx[i] and len(maxx[i]) == 3:
        m = max(m, sum(maxx[i]))
print(m)


print(maxx)
print(max(sum(maxx[0]), sum(maxx[1]), sum(maxx[2]), (max(maxx[0]) + max(maxx[1]) + max(maxx[2]))))