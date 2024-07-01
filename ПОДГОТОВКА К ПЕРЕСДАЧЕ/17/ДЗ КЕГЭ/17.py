f = open('17.txt')
f = [int(i) for i in f]

count = 0
mx = 0
mnmx = []
for i in sorted(f):
    if str(i)[-1] == '4':
        mnmx.append(i)

summa = max(mnmx) + min(mnmx)

for i in range(len(f) - 1):
    if (f[i] + f[i + 1]) < summa:
        count += 1
        mx = max(mx, (f[i] + f[i + 1]))

print(count, mx)