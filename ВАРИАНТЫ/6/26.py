f = open('26.txt')
s, n = list(map(int, f.readline().split()))
f = sorted([int(i) for i in f])

last = 0
count = 0
new = []
m_last = 0
for i in range(n):
    if sum(new) + f[i] <= s:
        new.append(f[i])
        count += 1
    else:
        last = new[-1]
        raznizca = s - sum(new)
        for j in range(i, n):
            m = f[i]
            if m - last > raznizca:
                m_last = f[i - 1]
                break

print(count, m_last)