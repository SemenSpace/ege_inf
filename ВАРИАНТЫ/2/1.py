from itertools import *

slovo = 'РОСОМАХА'
kol = 0
for j in set(permutations(slovo, r=8)):
    i = ''.join(j)
    if 'ОО' not in i and 'АА' not in i and 'РС' not in i and 'РМ' not in i and 'РХ' not in i and 'СМ' not in i and 'СХ' not in i and 'СР' not in i \
        and 'МР' not in i and 'МС' not in i and 'МХ' not in i and 'ХС' not in i and 'ХР' not in i and 'ХМ' not in i and 'ХХ' not in i and \
            'РР' not in i and 'СС' not in i and 'ММ' not in i and 'ОА' not in i and 'АО' not in i:
        kol += 1

print(kol)