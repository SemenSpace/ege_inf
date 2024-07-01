f = open('8.txt')
n = int(f.readline())
f = sorted([int(i) for i in f])

proc_70 = int(n * 0.7)
proc_50 = n // 2

sale_1 = []
sale_2 = []

for i in range(proc_70):
    sale_1.append(f[i]*0.7)
for i in range(proc_70, len(f)):
    sale_1.append(f[i]*0.6)

for i in range(proc_50):
    sale_2.append(f[i]*0.6)
for i in range(proc_50, len(f)):
    sale_2.append(f[i]*0.65)

print(sum(sale_1) - sum(sale_2))
print(max(sale_1))

