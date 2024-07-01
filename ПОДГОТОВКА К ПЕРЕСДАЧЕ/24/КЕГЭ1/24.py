f = open('24.txt').readline()

f = f.replace('BAD', '*** ').replace('FAT', '*** ').split()
mn = 10**20
for i in range(len(f) - 2):
    s = ''.join(f[i:i+3])
    s = s[s.index('*'):]
    mn = min(len(s), mn)

print(mn)