from itertools import *

k = 0
for i in product('АПРСУ', repeat=4):
    k += 1
    if i[0] == 'У':
        print(k)
        break