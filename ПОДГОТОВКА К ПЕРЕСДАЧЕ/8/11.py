from itertools import *

k = 0
gl = 'ИЯ'
for i in product('ВИШНЯ', repeat=6):
    if i.count('В') <= 1:
        if i[0] != 'Ш' and i[-1] not in gl:
            k += 1

print(k)