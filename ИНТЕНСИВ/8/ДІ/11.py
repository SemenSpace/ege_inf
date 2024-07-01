from itertools import *

ch = '2468'
nch = '1357'
k = 0
for i in product(ch, nch, ch, nch, ch, nch, ch, nch, ch):
    i = ''.join(i)
    flag = True
    for j in i:
        if i.count(j) > 3:
            flag = False
    if flag:
        k += 1

print(k * 2)