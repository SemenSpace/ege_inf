f = open('4.txt')
f = f.readline()

#f = 'aaaUaaUaaaUaaUaUaUaaUaaU'

ind = [i for i in range(len(f)) if f[i] == 'U']


m = 1000000000
for i in range(len(ind) - 109):
    dl = ind[i + 109] - ind[i] + 1
    m = min(m, dl)
print(m)