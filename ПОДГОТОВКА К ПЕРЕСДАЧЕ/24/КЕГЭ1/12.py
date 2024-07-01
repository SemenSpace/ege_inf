f = open('12.txt').readline()

k = 1
mx = 0
for i in range(1, len(f)):
    s1 = f[i - 1]
    s2 = f[i]
    if s2 >= s1:
        k += 1
    if (not(s2 >= s1)) or i == (len(f) - 1):
        mx = max(mx, k)
        k = 1

print(mx)