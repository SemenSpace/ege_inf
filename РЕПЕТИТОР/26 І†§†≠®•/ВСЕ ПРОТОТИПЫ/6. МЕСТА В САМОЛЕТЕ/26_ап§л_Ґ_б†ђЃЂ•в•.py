file = open("26_ряды_в_самолете.txt")
n, k = map(int, file.readline().split())
f = sorted([list(map(int, i.split())) for i in file])

s1 = { }
s2 = { }
for i in f:
    if i[0] == 1:
        if i[1] not in s1:
            s1[i[1]] = [i[2]]
        else:
            s1[i[1]] += [i[2]]

    if i[0] == 2:
        if i[1] not in s2:
            s2[i[1]] = [i[2]]
        else:
            s2[i[1]] += [i[2]]

max_num_in_row = 0
count_row = 0

for i in s1:
    if s1[i][0] > 4 or 6 - s1[i][-1] >= 4:
        max_num_in_row =max(max_num_in_row, i)
        count_row += 1

for i in s2:
    if s2[i][0] > 4 or 6 - s2[i][-1] >= 4:
        max_num_in_row =max(max_num_in_row, i)
        count_row += 1

print(max_num_in_row, count_row)