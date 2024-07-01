from itertools import *

k = 0
for i in product('ABCD', repeat=4):
    s = ''.join(i)
    s = s.replace('A', '1').replace('B', '2').replace('C', '3').replace('D', '4')
    if int(s[0]) <= int(s[1]) <= int(s[2]) <= int(s[3]):
        k += 1

print(k)