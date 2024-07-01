from fnmatch import fnmatch

def f(n: str):
    s = sum([int(i) for i in n])
    for x in range(2, s // 2):
        if s % x != 0:
            pass
        else:
            return 0
    return 1


for i in range(2627, 10**9, 2627):
    if f(str(i)) and fnmatch(str(i), '7*53?3*1'):
        print(i, i //2627)