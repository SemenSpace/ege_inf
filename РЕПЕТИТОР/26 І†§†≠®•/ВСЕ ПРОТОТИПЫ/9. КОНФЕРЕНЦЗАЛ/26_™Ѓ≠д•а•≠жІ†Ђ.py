file = open('КОНФЕРЕНЦЗАЛ.txt')
n = int(file.readline())
f = [[int(i.split()[1]) - int(i.split()[0]), int(i.split()[0]), int(i.split()[1])] for i in file]
f.sort()

zal = [0 for i in range(1441)]
last_time = []

count = 0
for i in f:
    razn, start, end = i
    if 1 not in zal[start:end]:
        last_time = [start, end]
        for j in range(start, end):
            zal[j] += 1
        count += 1
    else:
        if end > last_time[1] and start >= last_time[0]:
            last_time = [start, end]

        


print(count, last_time[1])