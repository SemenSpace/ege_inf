f = open('21.txt').readline()
f = f.replace('RO', '* ').split(' ')
print(f)
mx = 0

for i in range(len(f) - 21):
    s = ''.join(f[i:i + 21 + 1]).replace('*', 'RO')
    if 'ORO' not in s and 'ROR' not in s:
        mx = max(mx, len(s) - 1)

print(mx)
