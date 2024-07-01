from itertools import *

k = 0
for i in product('AB123', repeat=8):
    s = ''.join(i)
    s = s.replace('B', 'A')
    if s.count('A') == 2:
        k += 1

print(k)
