from itertools import *

k = 0
for i in product('ГЕПАРД', repeat=5):
    if i.count('Г') == 1 and i[0] != 'А' and i[-1] != 'Е':
        k += 1

print(k)

###################
k = 0
for a in 'ГЕПРД': # Удаляем символ из цикла (А)
    for b in 'ГЕПАРД':
        for c in 'ГЕПАРД':
            for d in 'ГЕПАРД':
                for e in 'ГПАРД': # Удаляем символ из цикла (Е)
                    s = a + b + c + d + e
                    if s.count('Г') == 1:
                        k += 1

print(k)
