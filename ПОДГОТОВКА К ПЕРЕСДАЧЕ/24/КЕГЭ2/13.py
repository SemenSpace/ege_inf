f = open('13.txt').readline()
k = 0
for i in range(len(f) - 6):
    if f[i] == 'A' and f[i + 6] == 'F':
        k += 1
for i in range(len(f) - 7):
    if f[i] == 'A' and f[i + 7] == 'F':
        k += 1
for i in range(len(f) - 8):
    if f[i] == 'A' and f[i + 8] == 'F':
        k += 1
for i in range(len(f) - 9):
    if f[i] == 'A' and f[i + 9] == 'F':
        k += 1
print(k)
