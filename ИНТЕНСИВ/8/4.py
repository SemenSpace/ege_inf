from itertools import *

k = 0
for i in set(permutations('01234567', r=5)):
    s = ''.join(i)
    s = s.replace('2', '0').replace('4', '0').replace('6', '0').replace('5', '3').replace('7', '3')
    if '1' not in s and s[0] != '0' and '00' not in s and '33' not in s:
        k += 1

print(k)

k = 0
for i in set(permutations('01234567', r=5)):
    k += 1

print(k)