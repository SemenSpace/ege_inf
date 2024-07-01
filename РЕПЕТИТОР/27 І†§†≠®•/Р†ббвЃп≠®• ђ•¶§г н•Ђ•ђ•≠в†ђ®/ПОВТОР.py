f = open('27_A (1).txt')
N = int(f.readline())
f = sorted([list(map(int, i.split())) for i in f])

mx = 0
mx_1 = 0

k = 5
s = sum([max(i) for i in f])

for i in f:
    mx = max(mx, sum(i) - max(i) - min(i))
for i in f:
    mx_1 = max(mx_1, max(i))
s = s - mx_1 + mx
if s % 109 == 0:
    print(s)









