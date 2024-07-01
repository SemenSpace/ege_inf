f = open('24.txt')
f = f.readline()

alp = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')[:24]
print(alp)


k = 0
mx = 0

for i in f:
    if i in alp:
        k += 1

    else:
        mx = max(mx, k)
        k = 0


print(mx)