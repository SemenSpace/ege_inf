from itertools import *

kon = []
k = 0
for i in product('АПРСУ', repeat=5):
    k += 1
    i = ''.join(i)
    if i.count('У') <= 1 and 'АА' not in i:
        kon.append([k, i])

print(kon)

print(int('43333', 5) + 1)