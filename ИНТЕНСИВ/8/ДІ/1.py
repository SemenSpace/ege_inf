from itertools import *

k = 0
for i in set(permutations('0123456789', r=4)):
    s = ''.join(i)
    s = s.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0').replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
    if '11' not in s and '00' not in s:
        k += 1

print(k)