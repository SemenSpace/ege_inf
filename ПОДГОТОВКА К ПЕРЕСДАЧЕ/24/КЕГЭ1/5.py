f = open('5.txt').readline()



k = 0
mx = 0
last = ''
for i in range(len(f)):

    if f[i] != 'P' or f[i] == 'P' and last != 'P':
        k += 1
    if f[i] == 'P' and last == 'P' or i == (len(f) - 1):
        mx = max(mx, k)
        k = 1
    last = f[i]
print(mx)