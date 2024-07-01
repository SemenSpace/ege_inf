from itertools import *

count = 0
for i in product('LOST', repeat=7):
    if i.count('O') == 3:
        count += 1

print(count)