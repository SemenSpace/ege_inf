f = open('18.txt').readline().split('D')
mx = 0

for i in range(len(f) - 2):
    k = 0
    for j in f[i:i+3]:
        k += len(j)
    mx = max(mx, k + 2)

print(mx)