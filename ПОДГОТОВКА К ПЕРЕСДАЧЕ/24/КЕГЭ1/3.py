f = open('3.txt').readline()
alp = '0123456789'

mx = 0
k = 0
for i in range(len(f)):
    if f[i] in alp:
        k += 1
    else:
        mx = max(mx, k)
        k = 0

print(mx)