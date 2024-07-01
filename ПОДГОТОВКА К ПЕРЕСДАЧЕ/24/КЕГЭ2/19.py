f = open('19.txt')
f = [str(i) for i in f]

mxQ = 0
last = ''

for i in f:
    if i.count('Q') > mxQ:
        mxQ = i.count('Q')
        last = i

alp = sorted('qwertyuiopasdfghjklzxcvbnm'.upper())

for i in range(len(alp)):
    alp[i] = alp[i][0] + '0'

for i in last:
    for j in range(len(alp)):
        if alp[j][0] == i:
            alp[j] = alp[j][0] + str(int(alp[j][1:]) + 1)
            break

mn = 'A10000000000'
for i in alp:
    s1 = int(i[1:])
    m = int(mn[1:])

    if s1 < m:
        mn = i

bukva = mn[0]
print(bukva, sum([i.count(bukva) for i in f]))