f = open('4.txt').readline()
ind = [int(i) for i in range(len(f)) if f[i] == 'U']



m = 10**10
for i in range(len(ind) - 109):
    dl = ind[i + 109] - ind[i] + 1
    m = min(m, dl)

print(m)