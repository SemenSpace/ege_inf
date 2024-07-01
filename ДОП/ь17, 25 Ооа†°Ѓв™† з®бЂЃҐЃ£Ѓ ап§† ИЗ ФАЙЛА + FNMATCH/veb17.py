f = open('17.5.txt')
# 2 2339
file = []
for i in f:
    file.append(int(i))

sum_pari = []
for i in range(len(file) - 1):
    if (file[i] > 0 and file[i] ** (1/3) % 1 == 0) or (file[i + 1] > 0 and file[i + 1] ** (1/3) % 1 == 0):
        sum_pari.append(file[i] + file[i + 1])

print(len(sum_pari), max(sum_pari))




# прикольная идея, но в чём-то ошибка
sum_twin = []
for i in range(len(file) - 1):
    if file[i] > 0 and file[i] > 0 and ((abs(file[i]) / abs(file[i]) / abs(file[i])) ** 3 == abs(float(file[i])) or
            (abs(file[i + 1]) / abs(file[i + 1]) / abs(file[i + 1])) ** 3 == abs(float(file[i + 1]))):
        sum_twin.append(file[i] + file[i + 1])

print(len(sum_twin), max(sum_twin), sum_pari)