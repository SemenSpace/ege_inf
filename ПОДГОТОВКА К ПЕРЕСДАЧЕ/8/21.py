from itertools import *
for n, i in enumerate(product('АИМРЯ', repeat=4), 1):
    if n == 211:
        print(i)