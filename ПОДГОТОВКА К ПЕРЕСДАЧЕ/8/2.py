from itertools import *

k = 0
b = 'WXYZ'
for i in product('ABCWXYZ', repeat=6):
    if i[0] in b and i[-1] in b and i[1] not in b and i[2] not in b and i[3] not in b and i[4] not in b:
        k += 1

print(k)