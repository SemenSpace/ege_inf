with open('17.txt') as file:
    f = file.read().split()
sorted(f)
print(sorted(f))
mx = 0
kol = 0
for x in range(len(f) - 1):
    for y in range(x + 1, len(f)):
        if (int(f[x]) * int(f[y])) % 10 == 0:
            kol += 1
            mx = max(mx, int(f[x]) + int(f[y]))

print(kol, mx)