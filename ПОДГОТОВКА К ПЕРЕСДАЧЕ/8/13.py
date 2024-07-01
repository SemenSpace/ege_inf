from itertools import *
k = 0
for i in product('ГЕПРАД', repeat=5):
    if i.count('Г') == 1:
        if i[0] != 'А' and i[-1] != 'Е':
            k += 1
print(k)