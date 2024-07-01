from itertools import *

k = 0
for i in product('01234567', repeat=12):
    if i[0] != '0':
        i = ''.join(i)
        i = i.replace('3', '1').replace('5', '1').replace('7', '1')
        if i.count('1') == 3 and '11' not in i:
            k += 1

print(k)