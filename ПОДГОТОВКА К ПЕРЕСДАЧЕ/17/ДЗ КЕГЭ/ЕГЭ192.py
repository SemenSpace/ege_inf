f = open('ЕГЭ192.txt')
f = [int(i) for i in f]

count = 0
mx = 0

big = 0
for i in f:
    if len(str(abs(i))) == 4 and str(i)[-1] == '7':
        big = max(big, i)

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]

    if (len(str(abs(s1))) == 4 and str(s1)[-1] == '7') + (len(str(abs(s3))) == 4 and str(s3)[-1] == '7')\
            + (len(str(abs(s2))) == 4 and str(s2)[-1] == '7') >= 2:
        if s1 + s2 + s3 > big:
            count += 1
            mx = max(mx, s1 + s2 + s3)

print(count, mx)