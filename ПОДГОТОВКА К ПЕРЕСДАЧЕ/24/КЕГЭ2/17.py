f = open('17.txt').readline()
alp = sorted('qwertyuiopasdfghjklzxcvbnm'.upper())

for i in range(len(alp)):
    alp[i] = alp[i] + '0'

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    if s1 == s3:
        for j in range(len(alp)):
            if alp[j][0] == s2:
                alp[j] = alp[j][0] + str(int(alp[j][1:]) + 1)

kon = 'A1468'
for i in alp:
    s1 = i[1:]
    k = kon[1:]
    if s1 > k:
        kon = i

print(kon)