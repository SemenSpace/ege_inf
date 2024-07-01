# РЕКУРСИЯ

def task_23(start, end):
    if start > end:  # мы уже никак не сможем попасть в конечное число, следовательно, в этом случае у нас ноль путей
        return 0

    if start == end:
        return 1

    if start < end:
        return task_23(start + 1, end) + task_23(start * 2, end)


print(task_23(1, 14))


##################################################################################################################################


def task_23_1(start, end):
    if start > end:
        return 0

    if start == end:
        return 1

    if start < end:
        return task_23_1(start + 1, end) + task_23_1(start * 3, end)


print(task_23_1(2, 56))


##################################################################################################################################

def task_23_2(start, end):
    if start > end:
        return 0

    if start == end:
        return 1

    if start < end:
        return task_23_2(start + 1, end) + task_23_2(start * 3, end) + task_23_2(start ** 2, end)


print(task_23_2(4, 93))


##################################### СОДЕРЖИТ И НЕ СОДЕРДИТ ЧИСЛО ###############################################################

def task_23_3(start, end):
    if start > end:
        return 0

    if start == 27:  # мы не проходим через 27 -> у нас ноль дорог в этом числе
        return 0

    if start == end:
        return 1

    if start < end:
        return task_23_3(start + 2, end) + task_23_3(start * 2, end)


print(task_23_3(3, 15) * task_23_3(15, 72))  # нам нужно пройти через 15 -> разделяем и перемножаем
