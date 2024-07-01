from itertools import *

k = 0
for i in product('САЛО', repeat=6):
    O = i.count('О')
    if 1 <= O <= 3:
        k += 1

print(k)