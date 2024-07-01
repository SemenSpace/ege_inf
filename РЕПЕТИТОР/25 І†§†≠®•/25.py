from fnmatch import *

def f(n):
    kon = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            kon.add(i)
    stepen = [2**i for i in range(1, 31)]
    if len(kon) not in stepen:
        return 1
    return 0


for i in range(2031, 10**9 + 1, 2031):
    s = str(i)
    if fnmatch(s, '*31*65?') and i % 31 == 0 and f(i):
        print(i, i // 2031)