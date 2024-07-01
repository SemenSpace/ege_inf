f = open('24.txt')
f = str(f.readline())
f = f.replace('R', 'Q').replace('W', 'Q').replace('2', '1').replace('4', '1')

count = 0
k = 1
for i in range(1, len(f)):
    if f[i] != f[i - 1]:
        k += 1
    else:
        count = max(count, k)
        k = 1

print(count)

f = f.replace('QQ', ' ').replace('11', ' ').split(' ')
