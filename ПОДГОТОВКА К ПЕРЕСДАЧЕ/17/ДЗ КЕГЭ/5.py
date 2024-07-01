f = open('5.txt')
f = [int(i) for i in f]

summa = 0
count = 0
for i in f:
    h = str(hex(i)[2:])
    if h[-1] == 'b':
        if i % 7 == 0 and i % 6 != 0 and i % 13 != 0 and i % 19 != 0:
            count+=1
            summa += i

print(summa, count)
