f = open("26.txt")
n = int(f.readline())
f = sorted([list(map(int, i.split())) for i in f])

okna = [[0 for h in range(1440)] for i in range(3)]


count = 0
count_leave = 0
for i in range(len(f)):
    nach, dl, win = f[i]
    if win != 0:
        if 14 not in okna[win][nach : nach + dl]:
            if win == 2:
                count += 1
            for j in range(nach, nach + dl):
                okna[win][j] += 1
        else:
            count_leave += 1
    else:
        kol_1 = max(okna[1][nach : nach + dl])
        kol_2 = max(okna[2][nach : nach + dl])
        if kol_1 == kol_2 and kol_1 < 14 or kol_2 > kol_1 and kol_1 < 14:
            for j in range(nach, nach + dl):
                okna[1][j] += 1

        elif kol_1 > kol_2 and kol_2 < 14:
            if 14 not in okna[2][nach : nach + dl]:
                if win == 2:
                    count += 1
                for j in range(nach, nach + dl):
                    okna[2][j] += 1
        else:
            count_leave += 1


print(count, count_leave)