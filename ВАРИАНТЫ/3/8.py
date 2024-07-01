from itertools import *

count = 0
last = ''
for i in product('ПОЛИНА', repeat=8):
    i = ''.join(i)
    if (i.count('П') + i.count('Л') + i.count('Н')) > (i.count('О') + i.count('И') + i.count('А')):
        count += 1
        last = i
print(count, last)