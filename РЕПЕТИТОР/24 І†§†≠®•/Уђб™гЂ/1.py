f = open('24_demo2021.txt')
s = f.readline()

kol = 1
mx = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        kol += 1
    else:
        mx = max(mx, kol)
        kol = 1

print(mx)