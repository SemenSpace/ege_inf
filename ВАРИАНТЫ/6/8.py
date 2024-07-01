from itertools import *

for n, i in enumerate(product('ЛНОС', repeat=4), 1):
    print(n, i)
    if n == 250:
        print(''.join(i))


n = 249
s = ''
while n > 0:
    s += str(249 % 4)
    n //= 4

print(list(s))
