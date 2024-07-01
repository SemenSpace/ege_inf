from itertools import *

k = 0
for i in set(permutations('123', r=3)):
    print(i)
    k += 1

print(k)