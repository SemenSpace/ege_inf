from itertools import *

k= 0
for i in product('0123456789', repeat=3):
    s = ''.join(i)
    if s[0] != '0':
        if int(s[0]) <= int(s[1]) <= int(s[2]):
            k += 1

print(k)