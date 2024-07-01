from itertools import *

ch = '02468'
nch = '1357'

count = 0
for i in product('012345678', repeat=7):
    if i.count('8') == 1 and i[0] not in nch and i[-1] not in ch and int(i[0]) >= 1:
        count += 1

print(count)