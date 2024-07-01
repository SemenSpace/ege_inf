from itertools import *
k=0
for n, i in enumerate(product('ЕЛМРУ', repeat=4), 1):
    if i[0] == 'Л':
        print(n)
        break