file = open('test')
m, n = map(int, file.readline().split())
f = [list(map(int, i.split())) for i in file]

max_time = 0
time = [0 for i in range(1441 * 2)]

max_count = 0
num_parking = [0 for i in range(m + 1)]
for i in f:
    start, prod, p1, p2 = i
    for j in range(start, start + prod):
        time[j] += 1
    num_parking[p1] += 1



print(time.index(max(time)), num_parking.index(max(num_parking)))




