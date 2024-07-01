from fnmatch import fnmatch

for i in range(4891, 10**10 + 1, 4891):
    if fnmatch(str(i), '1?7602*0'):
        print(i)
