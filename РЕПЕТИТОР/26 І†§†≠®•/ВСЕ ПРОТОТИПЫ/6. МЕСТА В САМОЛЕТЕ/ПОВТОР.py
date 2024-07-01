f = open('26_ряды_в_самолете.txt')
n, k = list(map(int, f.readline().split()))
f = [list(map(int, i.split())) for i in f]

first_flo = []
second_flo = []
for i in f:
    if i[0] == 1:
        first_flo.append(i)
    else:
        second_flo.append(i)
second_flo.sort()
first_flo.sort()


f_zan = [[]]
s_zan = [[]]
for i in first_flo:
    s = [0, 0, 0, 0, 0, 0]
    if i[1] not in f_zan[0]:
        f_zan[0].append(i[1])
        s[i[2]- 1] = 1
        f_zan.append([i[1], s])
    else:
        f_zan[-1][1][i[2] - 1] = 1

for i in second_flo:
    s = [0, 0, 0, 0, 0, 0]
    if i[1] not in s_zan[0]:
        s_zan[0].append(i[1])
        s[i[2]- 1] = 1
        s_zan.append([i[1], s])
    else:
        s_zan[-1][1][i[2] - 1] = 1

count = 0
last = 0
f_zan[0] = [1, [1, 1, 1, 1, 1, 1]]
s_zan[0] = [1, [1, 1, 1, 1, 1, 1]]


for i in f_zan:
    if 1 not in i[1][:4] or 1 not in i[1][2:]:
        count += 1
        last = max(last, i[0])

for i in s_zan:
    if 1 not in i[1][:4] or 1 not in i[1][2:]:
        count += 1
        last = max(last, i[0])

print(last, count)
