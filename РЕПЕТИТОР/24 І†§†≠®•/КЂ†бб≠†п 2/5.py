f = open('k8-1.txt')
f = f.readline()

count = 1
m = 0
for i in range(1, len(f)):
    if f[i] != f[i - 1]:
        count += 1
        m = max(m, count)
        continue
    count = 1

print(count)