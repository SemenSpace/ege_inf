from itertools import *

k = 0
for i in product('АВЕСТ', repeat=5):
    k += 1
    print(''.join(i))
    if ''.join(i) == 'СВЕТА':
        print(k)
        break

print(int('31240', 5) + 1)