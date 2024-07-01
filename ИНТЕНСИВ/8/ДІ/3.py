from itertools import *

k = 0
for i in product('АПРСУ', repeat=4):
    k += 1
    print(i)
    i = ''.join(i)
    if 'А' not in i:
        print(k)
        break
