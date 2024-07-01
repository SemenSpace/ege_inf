f = open('27-B.txt')
k, n = int(f.readline())*3, int(f.readline())
f = [int(i) for i in f if int(i) > 0]

s = sorted(f, reverse=True)

mx = s[0] + s[1]


count = 0
ind = f.index(s[1])
for i in range(2, len(s)):
    if abs(ind - f.index(s[i])) >= k:
        print(mx + s[i])
        break
