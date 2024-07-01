f = open('17.txt')
f = [int(i) for i in f]

m_kr = 0
m_sum = 0
count = 0
for i in sorted(f):
    if i % 19 == 0:
        m_kr = i
        break

for i in range(len(f) - 1):
    if f[i] % m_kr == 0 or f[i + 1] % m_kr == 0:
        count += 1
        m_sum = max(m_sum, f[i] + f[i+1])

print(count, m_sum)