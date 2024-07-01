f = open('27_A.txt')
N = int(f.readline())
f = [list(sorted(map(int, i.split()))) for i in f]

m = []
for i in f:
    m.append(i[0])
m.sort()

summa = 0
for i in f:
    summa += i[1]

for i in m:
    if summa % 13 == 0:
        summa -= i
    else:
        print(summa)
        break