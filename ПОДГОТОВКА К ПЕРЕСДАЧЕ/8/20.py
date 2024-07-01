from itertools import *
for n, i in enumerate(product('АИМРЯ', repeat=4), 1):
    s = ''.join(i)
    if s == 'АРИЯ':
        print(n, s)
