f = open('14.txt')
f = [int(i) for i in f]

count = 0
sr = sum(f)/len(f)
ans = []

for i in range(len(f) - 2):

    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]

    if ((s1 > sr) + (s2 > sr) + (s3 > sr)) >= 2:
        count += 1
        ans.append(s1 + s2 + s3)

print(count, max(ans))
