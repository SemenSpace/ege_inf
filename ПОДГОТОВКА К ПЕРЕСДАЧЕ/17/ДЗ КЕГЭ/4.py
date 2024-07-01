f = open('4.txt')
f = [int(i) for i in f]

count = 0
mx = 0
mn = 10**10

for i in f:
    if i % 13 == 7 and i % 7 != 0 and i % 11 != 0:
        count += 1
        mx = max(mx, i)
        mn = min(mn, i)

print(mx - mn, count)