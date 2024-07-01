f = open('zadanie24_2.txt')
s = f.readline()

kol = 1
mx = 1
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        kol += 1
        mx = max(mx, kol)
    else:
        kol = 1

print(mx)