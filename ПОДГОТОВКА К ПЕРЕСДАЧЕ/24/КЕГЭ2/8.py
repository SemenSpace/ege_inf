f = open('8.txt').readline()
k = 0
for i in range(len(f) - 4):
    s1 = f[i]
    s3 = f[i + 2]
    s5 = f[i + 4]
    if s1 == s3 == s5 == 'A':
        k += 1
print(k)