f = open("18.txt")
n = int(f.readline())
f = [
    [int(i.split()[1]) - int(i.split()[0]), int(i.split()[0]), int(i.split()[1])]
    for i in f
]

k = 0
time_line = [0] * 1441
last_start = 0
for i in sorted(f):
    rz, start, stop = i
    if last_start == start:
        for x in range(start, stop):
            if time_line[x] != 1:
                time_line[x] += 1
    else:
        if 1 not in time_line[start:stop]:
            k += 1
            for x in range(start, stop):
                if time_line[x] != 1:
                    time_line[x] += 1
                    last_start = start

print(time_line)

last = 0
for i in range(len(time_line)):
    if time_line[i] == 1:
        last = max(last, i)
print(k, last + 1)
