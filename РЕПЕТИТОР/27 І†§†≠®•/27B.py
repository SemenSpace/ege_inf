f = open('test.txt')
n = int(f.readline())
a = [int(i) for i in f]

print(a)

pref_left = [float('-inf')] * n
pref_right = [float('-inf')] * n

for i in range(n):
    pref_left[i] = max(pref_left[i - 1], a[i])

pref_right[n - 1] = a[-1]
for i in range(n - 2, -1 -1):
    pref_right[i] = max(pref_right[i + 1], a[i])

res = float('-inf')
for i in range(1, n - 1):
    if pref_left[i - 1] > a[i] and pref_right[i + 1] > a[i]:
        res = max(res, (pref_left[i - 1] + pref_right[i + 1] - 2 * a[i]))
        print(res, pref_left[i - 1], a[i], pref_right[i + 1])
print(res)



