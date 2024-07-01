from itertools import *

count = 0
gl = 'ЕО'
sogl = 'КРСЛ'
for i in product('КРЕСЛО', repeat=4):
    if i[0] in sogl and i[-1] in gl:
        count += 1
print(count)