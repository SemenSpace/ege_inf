f = open('ds17.txt')
file = [int(i) for i in f]
sum_troek = []
for i in range(len(file) - 2):
    if file[i] % 8 == 0 and file[i + 1] % 8 != 0 and file[i + 2] % 8 != 0:
        for j in range(5, 1000):
            if file[i + 1] % j == 0 and file[i + 2] % j == 0:
                sum_troek.append(file[i] + file[i + 1] + file[i + 2])
    if file[i] % 8 != 0 and file[i + 1] % 8 == 0 and file[i + 2] % 8 != 0:
        for x in range(5, 1000):
            if file[i] % x == 0 and file[i + 2] % x == 0:
                sum_troek.append(file[i] + file[i + 1] + file[i + 2])
    if file[i] % 8 != 0 and file[i + 1] % 8 != 0 and file[i + 2] % 8 == 0:
        for y in range(5, 1000):
            if file[i] % y == 0 and file[i + 1] % y == 0:
                sum_troek.append(file[i] + file[i + 1] + file[i + 2])

print(len(sum_troek), max(sum_troek))