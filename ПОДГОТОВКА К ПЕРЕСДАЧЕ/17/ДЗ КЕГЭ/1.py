f = open('1.txt')
f = [int(i) for i in f]

mx = 0
count = 0
for i in f:
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        count += 1
        mx = max(mx, i)

print(count, mx)