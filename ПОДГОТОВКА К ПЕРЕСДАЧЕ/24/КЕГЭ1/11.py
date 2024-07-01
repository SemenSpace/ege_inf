f = open('11.txt').readline()
k = 1
mx = 0


for i in range(1, len(f)):
    s1 = f[i]
    s2 = f[i - 1]

    if s1 != s2:
        k += 1
    if s1 == s2 or i == (len(f) - 1):
        mx = max(mx, k)
        k = 1

print(mx)