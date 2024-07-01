f = open("19.1.txt")
n = int(f.readline())
f = [list(map(int, i.split())) for i in f]
#    0. артикул 1.цена 2.статус
sr = sum([i[1] for i in f]) / len(f)


prodan = []
ostat = []
for i in f:
    if float(i[1]) > sr:
        if i[2] == 0:
            prodan.append(i)
        else:
            ostat.append(i)


mx_art = 0
mx_price = 0
art = []
mx_count_art = []

for i in prodan:
    art.append(i[0])
for i in art:
    if art.count(i) >= mx_art:
        mx_art = art.count(i)

for i in prodan:
    if art.count(i[0]) == mx_art:
        if i[0] not in mx_count_art:
            mx_count_art.append(i[0])

mx_price_art = []
for i in prodan:
    art, price, stat = i
    if art in mx_count_art and [price, art] not in mx_price_art:
        mx_price_art.append([price, art])
mx_price_art.sort(reverse=True)
mx_price_last = mx_price_art[0][0]

mn_ostat = 10**10
lider_prodazh = []
print(mx_price_art)

b = 0
for i in mx_price_art:
    if i[0] == mx_price_last:
        b += 1
    else:
        mx_price_art.remove(i)
if b != 1:
    for i in mx_price_art:
        price, art = i
        k = 0
        for x in ostat:
            if x[0] == art:
                k += 1
        if k < mn_ostat:
            mn_ostat = k
            lider_prodazh = i
else:
    lider_prodazh = mx_price_art[0]
    mn_ostat = 0
    for x in ostat:
        if x[0] == lider_prodazh[1]:
            mn_ostat += 1
print(lider_prodazh)

art_prod = lider_prodazh[1]
price_prodan = lider_prodazh[0]
s = 0
for i in ostat:
    if i[0] == art_prod:
        s += price_prodan
print(s, art_prod)
