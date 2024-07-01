from itertools import *

k = 0
for i in permutations('АБИКОЛУН', r=8):
    s = ''.join(i)
    s = s.replace('И', 'А').replace('О', 'А').replace('У', 'А')
    s = s.replace('К', 'Б').replace('Л', 'Б').replace('Н', 'Б')

    if 'АА' not in s and 'ББ' not in s:
        k +=1
print(k)