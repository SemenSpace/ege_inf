f = open('3.txt').readline()
f = f.replace('A', 'A ').replace('B', 'B ').split()

m = 0
for i in range(len(f) - 2):
    s = f[i] + f[i + 1] + f[i + 2][:-1]
    if s.count('A') == 1 and s.count('B') == 1:
        m = max(m, len(s))

print(m)