# 123*5*
from fnmatch import *


for i in range(1001, 550000):
    if fnmatch(str(i), '53?12*') and i % 56 == 0:
        print(i, (int(str(i)[:2]) * int(str(i)[-2:])))


