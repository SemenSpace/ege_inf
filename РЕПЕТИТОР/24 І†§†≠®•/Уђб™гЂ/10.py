f = open('24_ege2022_day2.txt').readline()

file = f.replace('NPO', 'PNO')

for i in range(100000):
    if i*'PNO' in file:
        print(i)