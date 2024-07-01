f = open('k7c-1.txt')
f = f.readline()

s1 = 'BCD'
s2 = 'BDE'
s3 = 'BCE'

count = 0
for i in range(2, len(f)):
    if f[i - 2] in s1:
        if f[i - 1] in s2 and f[i - 1] != f[i - 2]:
            if f[i] in s3 and f[i] != f[i - 1]:
                count += 1

print(count)