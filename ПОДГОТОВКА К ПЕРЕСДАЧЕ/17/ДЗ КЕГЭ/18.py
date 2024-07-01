f = open('18.txt')
f = [int(i) for i in f]

count = 0
mx = 0

for i in range(len(f) - 1):
    s1 = f[i]
    s2 = f[i + 1]
    if (s1 % 9 == 0 and s2 % 9 != 0 and str(oct(s2)[-1]) == '3')\
        or (s1 % 9 != 0 and s2 % 9 == 0 and str(oct(s1)[-1]) == '3'):
        count += 1
        mx = max(mx, s1, s2)

print(count, mx)