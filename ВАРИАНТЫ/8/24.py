f = open('24.txt')
f = f.readline()

f = f.replace('R', 'Q').replace('W', 'Q').replace('2', '1').replace('4', '1')
# 1 и Q

k = 1
mx = 0
for i in range(1, len(f)):
    if f[i] != f[i - 1]:
        k += 1
    else:
        mx = max(mx, k)
        k = 1

print(mx)