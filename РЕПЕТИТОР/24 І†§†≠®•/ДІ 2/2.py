f = open('2.txt')
f = f.readline()

sogl = 'CDF'
gl = 'AO'

count = m = 0
for i in range(2, len(f), 3):
    x, y, z = f[i - 2], f[i - 1],  f[i]
    if x in sogl and y in sogl and z in gl:
        count += 1
    else:
        m = max(m, count)
        count = 0

print(m)