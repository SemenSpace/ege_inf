f = open('6.txt')
f = f.readline()

f = f.replace('Y', 'Y ')
f = f.split()

dl = 0
for i in range(len(f) - 150):
    dl = max(dl, sum([len(j) for j in f[i:i+150]]))

print(dl)
