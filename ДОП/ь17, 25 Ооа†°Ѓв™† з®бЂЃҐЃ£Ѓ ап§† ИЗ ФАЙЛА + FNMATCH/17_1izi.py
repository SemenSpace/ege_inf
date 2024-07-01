# задание 17
# прототип с парами чисел


f = open('17.1.txt')  # открываем файлик
a = []
for s in f:
    a.append(int(s))  # добавляем каждую срочку в int


sum_twin = []
for i in range(0, len(a) - 1):  # -1 чтобы предпоследний элемент взял себе в 'twin' последний
    if a[i] % 11 == 0 and a[i + 1] % 11 == 0:
        sum_twin.append(a[i] + a[i + 1])

# нужен модуль числа abs(int(x))

print(len(sum_twin), min(sum_twin))
