def d(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[0]


f = open("10.txt")
f = [int(i) for i in f]

count = 0
mn = 0

for i in range(len(f) - 2):
    s1 = f[i]
    s2 = f[i+1]
    s3 = f[i+2]

    if s1 % 3 == 2 or s2 % 3 == 2 or s3 % 3 == 2:
        count += 1
        mn += min(s1, s2, s3)

print(count, mn)
