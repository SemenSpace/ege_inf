from itertools import *

k = 0
for i in product('ЛНОС', repeat=5):
    i = ''.join(i)
    k += 1
    if k == 1020:
        print(i)