f = open('24_aprobation_2022_2.txt').readline()

file = f.replace('BA', 'DA')
for i in range(1000):
    if i*'DA' in file:
        print(i)