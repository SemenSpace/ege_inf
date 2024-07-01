f = open('7.txt').readline()
k = 0
for i in range(len(f) - 3):
    s1 = f[i]
    s3 = f[i + 2]
    s4 = f[i + 3]
    if s1 + s3 + s4 == 'GME':
        k += 1
print(k)