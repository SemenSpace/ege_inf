from fnmatch import *


def f1(n):
    n = int(n)
    k = 0
    s = 0
    for x in range(2, n // 2, 2):
        if n % x == 0:
            k += 1
            s += x

    if k >= 4:
        return s
    return 0


count = 0
for i in range(65000, 10**1000000):
    if fnmatch(str(i), "6*97*5?"):
        z = f1(str(i))
        if z != 0:
            count += 1
            if count <= 7:
                print(i, z)
            else:
                exit()
