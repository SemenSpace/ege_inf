f = open('24_ege2022_day1.txt').readline()

file = f.replace('A', 'O')
file = file.replace('B', 'C')
file = file.replace('D', 'C')

for i in range(100000): # СОГЛАСНАЯ + ГЛАСНАЯ!!!
    if i*'CO' in file:
        print(i)