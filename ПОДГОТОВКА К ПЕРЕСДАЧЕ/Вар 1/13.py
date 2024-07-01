from itertools import *

count = 0
for i in product('01', repeat=12):
    if i.count('1') == 3:
        count += 1

print(count)

