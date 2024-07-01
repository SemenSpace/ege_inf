f = open("8.txt")
f = [int(i) for i in f]

count = 0
mx = 0

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    su = s1 + s2 + s3
    if str(su)[-1] == '5':
        if (s1 * s2 * s3) % 7 == 0:
            count += 1
            mx = max(mx, su)
print(count, mx)