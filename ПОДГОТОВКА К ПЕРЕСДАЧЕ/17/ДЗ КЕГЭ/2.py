f = open('2.txt')
f = [int(i) for i in f]

count = 0
mn = 10**10
for i in f:
    s = str(i)
    if i % 3 == 0 and i % 11 == 0 and (s[-1] == '2' or s[-1] == '7'):
        count += 1
        mn = min(mn, i)

print(count, mn)