f = open('24.txt')
f = str(f.readline())

f = f.replace('D', '*').split('*')

m = 0
for i in f:
    count = 1
    for j in range(1, len(i)):
        if i[j] != i[j - 1]:
            count += 1
        else:
            m = max(count, m)

print(m)