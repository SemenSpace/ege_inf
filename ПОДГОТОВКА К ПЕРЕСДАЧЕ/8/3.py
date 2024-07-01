from itertools import *

k = 0
for i in product('ПУЛЯ', repeat=6):
    y = i.count('У')
    if y == 2:
        k += 1

print(k)