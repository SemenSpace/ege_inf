from itertools import *

k = 0
for a in 'АНДРЕЙ':
    for b in 'АНДРЕЙ':
        for c in 'АНДРЕЙ':
            for d in 'АНДРЕЙ':
                for e in 'АНДРЕЙ':
                    for f in 'АНДРЕЙ':
                        s = a + b + c + d + e + f
                        if (s.count('А') >= 1) and (s.count('Й') <= 1):
                            k += 1
print(k)

#######################################################################

k = 0
for i in product('АНДРЕЙ', repeat=6):
    if (i.count('А') >= 1) and (i.count('Й') <= 1):
        k += 1

print(k)
