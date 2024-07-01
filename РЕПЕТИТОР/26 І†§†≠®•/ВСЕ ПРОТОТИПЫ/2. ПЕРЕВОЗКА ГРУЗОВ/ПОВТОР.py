f = open('26_2.txt')
N, M = list(map(int, f.readline().split()))
f = [int(i) for i in f]

dvesti = []
ostatok = []

for i in f:
    if 210 <= i <= 220:
        dvesti.append(i)
    else:
        ostatok.append(i)

M_ost = M - sum(dvesti)
ostatok.sort()
last = 0
count = len(dvesti)

for i in ostatok:
    if M_ost - i >= 0:
        last = i
        count += 1
        M_ost -= i
    else:
        print(last, M_ost, count)
        print(ostatok)
        break

print(count, M)
