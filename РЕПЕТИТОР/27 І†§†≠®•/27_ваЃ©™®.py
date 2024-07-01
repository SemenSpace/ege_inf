f = open('27_B.txt')
n = int(f.readline())
f = [list(map(int, i.split())) for i in f]

m = 0

for i in f:
    m += max(i)

if m % 109 != 0:
    print(m)