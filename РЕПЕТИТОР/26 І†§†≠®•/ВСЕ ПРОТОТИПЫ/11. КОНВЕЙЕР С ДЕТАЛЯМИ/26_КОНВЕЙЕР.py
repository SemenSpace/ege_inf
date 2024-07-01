file = open("26_КОНВЕЙЕР.txt")
n = int(file.readline())

num = 0
f = []
for i in file:
    num += 1
    a = i.split()
    f.append([int(a[0]), int(a[1]), num])

posled = []
for i in f:
    posled.append([i[0], 0, i[2]])
    posled.append([i[1], 1, i[2]])
posled.sort()

lenta = [0 for i in range(n + 1)]
last_num = 0
nums = []

for i in posled:
    if i[2] not in nums:
        nums.append(i[2])
        last_num = i[2]
        if i[1] == 0:
            for j in range(0, n + 1):
                if lenta[j] != 1:
                    lenta[j] += 1
                    break
        elif i[1] == 1:
            for j in range(n, -1, -1):
                if lenta[j] != 2:
                    lenta[j] += 2
                    break
        if last_num == 448:
            print(i)

print(last_num, lenta.count(1) - 1)
