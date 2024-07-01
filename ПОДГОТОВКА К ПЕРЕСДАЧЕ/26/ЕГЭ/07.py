f = open("07.txt")
n, r_kol, m_kol = map(int, f.readline().split())
f = sorted([[int(i.split()[1]), int(i.split()[0])] for i in f])
#            занятое место              ряд

lines = [10**10 for i in range(m_kol + 1)]
for i in f:
    place, row = i
    if lines[place] > row:
        lines[place] = row


mx_ryad = 0
mx_mesto = 0

for i in range(len(lines) - 1):
    r = min(lines[i], lines[i + 1]) - 1
    m = i + 1
    if r > 0:
        if r > mx_ryad:
            mx_ryad = r

plan_zalla = [[0 for i in range(m_kol + 1)] for i in range(r_kol + 1)]

for i in f:
    place, row = i

    plan_zalla[row][place] = 1

for i in range(len(plan_zalla[mx_ryad])):
    k = 0
    for x in range(mx_ryad, 0, -1):
        if plan_zalla[x][i] == 0:
            k += 1
    if plan_zalla[mx_ryad][i] == 0 and k == mx_ryad:
        mx_mesto = max(mx_mesto, i)

print(mx_ryad, mx_mesto)

