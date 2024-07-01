from itertools import *
k= 0
for i in permutations('ВАЙФУ', r=4):
    s = ''.join(i)
    if i[0] != 'Й' and 'ВФ' not in s and 'ФВ' not in s:
        k+=1
print(k)