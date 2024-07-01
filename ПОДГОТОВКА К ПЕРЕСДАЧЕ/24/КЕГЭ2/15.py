f = open("15.txt").readline()
alp = sorted("QWERTYUIOPASDFGHJKLZXCVBNM")

kon = 'A38408'
for i in range(len(alp)):
    alp[i] = alp[i][0] + str(f.count(alp[i][0]))

for i in alp:
    s1 = i[1:]
    mx = kon[1:]
    if s1 > mx:
        kon = i
print(kon)


