from itertools import *

k = 0
for i in set(permutations('ПОЛИНА', r=6)):
    i = ''.join(i)
    i = i.replace('Л', 'П').replace('Н', 'П').replace('И', 'О').replace('А', 'О')
    if 'ОО' not in i and 'ПП' not in i:
        k += 1

print(k)