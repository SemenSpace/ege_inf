f = open('7.txt')
f = [int(i) for i in f]

count = 0
mx = 0
max_15 = 0
for i in sorted(f, reverse=True):
    if i % 100 == 15:
        max_15 = i
        break

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]

    if (len(str(abs(s1))) == 4) + (len(str(abs(s2))) == 4) + (len(str(abs(s3))) == 4) == 1:
        su = s1 + s2 + s3
        if su >= max_15:
            count += 1
            mx = max(mx, su)

print(count, mx)