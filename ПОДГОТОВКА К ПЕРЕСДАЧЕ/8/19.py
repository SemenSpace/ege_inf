from itertools import *
for n, i in enumerate(product('АГИЛМОРТ', repeat=4), 1):
    s = ''.join(i)
    if s[-2] == 'И' and s[-1] == 'М':
        print(n, s)