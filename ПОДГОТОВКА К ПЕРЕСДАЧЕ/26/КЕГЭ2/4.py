f = open('1.txt')
n = int(f.readline())
f = sorted([int(i) for i in f])

pol = f[:n//2]
chet = f[n//4 * 3:]

k = 0
mn = 100**10

half = max(pol)
quatro = min(chet)


for x in range(len(f) - 1):
    for y in range(x + 1, len(f)):
        s1 = f[x]
        s2 = f[y]
        sr = int((s1 + s2)/2)
        if (s1 + s2) % 2 == 0:
            if half < sr:
                if sr < quatro:
                    mn = min(mn, sr)
                    k += 1

print(k, mn)
