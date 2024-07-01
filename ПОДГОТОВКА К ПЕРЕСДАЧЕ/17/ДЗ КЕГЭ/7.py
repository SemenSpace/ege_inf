f = open('7.txt')
f = [int(i) for i in f]
count = 0
mn = 10**10

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    pro = s1 * s2
    if pro > 0:
        if (s1 + s2) % 7 == 0:
            count += 1
            mn = min(mn, pro)
print(count, mn)