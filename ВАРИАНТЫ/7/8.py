from itertools import *

for n, i in enumerate(product('ЛНОС', repeat=4), 1):
    s = ''.join(i)
    print(n, i)