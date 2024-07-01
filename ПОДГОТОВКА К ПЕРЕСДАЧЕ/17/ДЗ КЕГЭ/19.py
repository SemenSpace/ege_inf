f = open('19.txt')
f = [int(i) for i in f]

count = 0
mx = 0

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]

    if s2 > 0 and str(s2)[-1] == '9' and (s1 <= 0 or str(s1)[-1] != '9') and (s3 <= 0 or str(s3)[-1] != '9'):
        count += 1
        mx = max(mx, s1 + s2 + s3)

print(count, mx)