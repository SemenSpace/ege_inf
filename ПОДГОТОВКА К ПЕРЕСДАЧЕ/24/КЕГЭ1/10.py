f = open("10.txt").readline().replace("N", "O").replace("P", "O").replace("O", "*")

k = 1
mx = 0
for i in range(1, len(f)):
    s1 = f[i - 1]
    s2 = f[i]
    if s1 != "*" or s2 != "*":
        k += 1
    if s1 == s2 and s1 == "*":
        mx = max(mx, k)
        k = 1
    if i == (len(f) - 1):
        mx = max(mx, k)

print(mx)