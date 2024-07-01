f = open('5.txt').readline()

k = 0

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    if s1 + s2 + s3 == 'XIX':
        k += 1
print(k)