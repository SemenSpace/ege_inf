f = open("14.txt").readline()
k = 0

for i in range(len(f) - 4):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    s4 = f[i + 3]
    s5 = f[i + 4]
    if s1 == s5 and s2 == s4:
        k += 1
print(k)
