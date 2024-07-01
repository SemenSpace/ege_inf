from itertools import *

k= 0
for i in permutations('0234567', r=5):
    s = ''.join(i)
    s = s.replace('2', '0').replace('4', '0').replace('6', '0')
    s = s.replace('5', '3').replace('7', '3').replace('1', '3')
    if i[0] != '0' and '1' not in i:
        if '33' not in s and '00' not in s:
            k += 1
print(k)
