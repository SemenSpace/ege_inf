f = open('5.txt')
f = f.readline()

ind = [i for i in range(len(f)) if f[i:i+2] == 'TT']


m = 1000000000
for i in range(len(ind) - 149):
    dl = ind[i + 149] - ind[i] + 2
    m = min(m, dl)
print(m)