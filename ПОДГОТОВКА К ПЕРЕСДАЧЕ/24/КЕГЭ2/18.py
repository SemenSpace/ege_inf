f = open("18.txt").readline()
alp = sorted("qwertyuiopasdfghjklzxcvbnm".upper())

for i in range(len(alp)):
    alp[i] = alp[i] + "0"

for i in range(len(f) - 4):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    s4 = f[i + 3]
    s5 = f[i + 4]

    if s1 == s5 == "C" and s2 == s4 == "B":
        for k in range(len(alp)):
            if alp[k][0] == str(s3):
                alp[k] = alp[k][0] + str(int(alp[k][1:]) + 1)
print(alp)
