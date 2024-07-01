f = open('23.txt').readline()
mn = 10**20

k = 0
l = 0

for r in range(len(f)):
    if f[r] == 'Y':
        k = 0
        l = r + 1
    if f[r] == 'X':
        k += 1
    while k >= 500:
        mn = min(mn, r - l + 1)
        if f[l] == 'X':
            k -= 1
        l += 1
print(mn)