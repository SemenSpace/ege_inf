f = open('19.txt').readline().split('T')

mx = 0
for i in range(len(f) - 100):
    k = 0
    s = len(''.join(f[i:i + 101])) + 100
    mx = max(mx, s)
print(mx)
