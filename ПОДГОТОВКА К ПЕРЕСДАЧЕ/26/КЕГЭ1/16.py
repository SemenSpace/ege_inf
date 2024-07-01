f = open('16.txt')
n = int(f.readline())
f = sorted([int(i) for i in f], reverse=True)
print(sorted(f))

d = 56
count = 1
last = 0
s1 = f[0]
for i in range(1, len(f)):
    s2 = f[i]
    if s1 - s2 >= d:
        count += 1
        s1 = f[i]
        last = f[i]

print(count, last)