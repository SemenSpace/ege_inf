"""f = open('19.txt').readline().split('T')

mx = 0
for i in range(len(f) - 100):
    k = 0
    s = len(''.join(f[i:i + 101])) + 100
    mx = max(mx, s)
print(mx)
"""
f = '012345678'
i = 6
print(f[i] + f[i + 1:i + 3])

print(len('QWERTYUIOPASDFGHJKLZXCVBNM'))

i = 0
print('123456789'[i:i + 9])