f = open("16.txt")
f = [int(i) for i in f]

mn11 = 10**10
count11 = 0
mx17 = 0
count17 = 0

for i in f:
    if i % 11 == 0:
        count11 += 1
        mn11 = min(mn11, i)
    if i % 17 == 0:
        count17 += 1
        mx17 = max(mx17, i)

if count11 > count17:
    print(count11, mn11)
else:
    print(count17, mx17)
