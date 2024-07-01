file = open("26_камеры_с_ячейками.txt")
k, n = int(file.readline()), int(file.readline())
f = sorted([list(map(int, i.split())) for i in file])

yach = ["0" * 1441 for i in range(k)]
last_yach = 0
count_pass = 0

for i in f:
    start, end = i
    for j in range(k):
        if "1" not in yach[j][start : end + 1]:
            yach[j] = yach[j][:start] + "1" * (end - start + 1) + yach[j][end + 1 :]
            count_pass += 1
            last_yach = j + 1
            break

print(count_pass, last_yach)