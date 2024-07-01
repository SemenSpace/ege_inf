f = open('22.txt').readline().replace('.', '. ').split(' ')
mn = 10**10
for i in range(len(f) - 6):
    s = len(''.join(f[i:i+7])) - len(f[i]) + 1
    mn = min(mn, s)
print(mn)