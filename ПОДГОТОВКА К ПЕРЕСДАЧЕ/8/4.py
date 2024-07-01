from itertools import *

k = 0
for i in product('ЛОДКА', repeat=4):
    o = i.count('О')
    if o >= 2:
        k += 1
print(k)