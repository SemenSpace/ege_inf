f = open('1.txt')
f = f.readline()

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph_24 = '0123456789ABCDEFGHIJKLMN'

count = m = 0
for i in f:
    if i in alph_24:
        count += 1
    else:
        m = max(m, count)
        count = 0

print(m)
