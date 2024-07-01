f = open("27_B.txt")
n = int(f.readline())
f = [list(sorted(map(int, i.split()))) for i in f]

m = 0
mn = 10**10
for i in f:
    m += max(i)
    s1 = i[2] - i[1]
    s2 = i[2] - i[0]
    if s1 % 109 != 0 and s1 != 0:
        mn = min(mn, s1)
    elif s2 % 109 != 0 and s2 != 0:
        mn = min(mn, s2)


if (m - mn) % 109 != 0:
    print(m - mn)
