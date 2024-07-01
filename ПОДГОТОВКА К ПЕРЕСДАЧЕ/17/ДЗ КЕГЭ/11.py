f = open("11.txt")
f = [int(i) for i in f]

count = 0
mn = 10**10


for i in range(len(f) - 3):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    s4 = f[i + 3]

    if s1 > s2 > s3 > s4:
        if max(s1, s2, s3, s4) - min(s1, s2, s3, s4) > 1000:
            count += 1
            mn = min(mn, s1 + s2 + s3 + s4)


print(count, mn)
