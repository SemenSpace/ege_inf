from itertools import *

k = 0
for i in product('012345678', repeat=5):
    i = ''.join(i)
    if i.count('3') == 2 and i[0] != '0':
        i = i.replace('3', '1').replace('5', '1').replace('7', '1')
        if '12' not in i and '21' not in i and '121' not in i:
            k += 1

print(k)