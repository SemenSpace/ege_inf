f = open('6.txt').readline()
k = 0

for i in range(len(f) - 3):
    if f[i] == f[i + 1] == f[i + 2] == f[i + 3] == 'X':
        k += 1
print(k)