f = open('3.txt')
f = [int(i) for i in f]
count = 0
mx = 0
mn = 10**10

for i in f:
    s = str(i)
    if i % 9 != 0 and i % 11 != 0 and (s[-1] == '5' or s[-1] == '7'):
        count += 1
        mx = max(mx, i)
        mn = min(mn, i)

print(count, mx + mn)