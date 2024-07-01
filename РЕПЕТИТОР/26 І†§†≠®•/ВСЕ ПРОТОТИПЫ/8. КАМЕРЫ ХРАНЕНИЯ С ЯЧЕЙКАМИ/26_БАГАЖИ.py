file = open("26-111.txt")
kol, n = int(file.readline()), int(file.readline())

f = [list(map(int, i.split())) for i in file]
yach = [1441 * "0" for i in range(kol)]
f.sort()

count = 0
last = ""

for i in f:
    start, end = i
    for j in range(kol):
        if "1" not in yach[j][start : end + 1]:
            count += 1
            last = j + 1
            yach[j] = yach[j][:start] + "1"*(end - start + 1) + yach[j][end + 1:]
            break

print(count, last)
