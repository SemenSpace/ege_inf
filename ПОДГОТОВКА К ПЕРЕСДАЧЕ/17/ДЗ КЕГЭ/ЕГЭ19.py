f = open('ЕГЭ19.txt')
f = [int(i) for i in f]

count = 0
mx = 0

big = 0
for i in f:
    if len(str(abs(i))) == 3:
        if i % 10 == 3:
            big = max(big, i)

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i+2]

    if (len(str(abs(s1))) == 3 and abs(s1) % 10 == 3) \
            or (len(str(abs(s2))) == 3 and abs(s2) % 10 == 3) \
            or (len(str(abs(s3))) == 3 and abs(s3)% 10 == 3):
        if s1 + s2 + s3 < big:
            count += 1
            mx = max(mx, s1 + s2 + s3)

print(count, mx)