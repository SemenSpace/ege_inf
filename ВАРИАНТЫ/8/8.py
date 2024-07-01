from itertools import *


sogl = 'КНРС'
k = 0
for n, i in enumerate(product('АЕКНРС', repeat=10), 1):
    if n % 3 == 0 and list(i)[0] in sogl and list(i).count('Р') == 1:
        k += 1

print(k)
