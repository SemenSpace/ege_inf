from fnmatch import *

for i in range(129, 10**8, 129):
    if fnmatch(str(i), '12?3*46'):
        print(i, i // 129)

