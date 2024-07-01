f = open('9.txt')
f = [int(i) for i in f]
count = 0
sr = 10 ** 10

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i + 1]
    s3 = f[i + 2]
    if s1 % 12 == 0 or s2 % 12 == 0 or s3 % 12 == 0:
        if s1 % 3 == 0 and s2 % 3 == 0 and s3 % 3 == 0:
            count += 1
            sr = min(sr, (s1 + s2 + s3)//3)

print(count, sr)