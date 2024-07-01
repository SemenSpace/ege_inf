f = open('20.txt').readline()

f = f.replace('AB', 'A B').split(' ')
mx = 0

for i in range(len(f) - 50):
    s = len(''.join(f[i:i + 51]))
    mx = max(mx, s)

print(mx)