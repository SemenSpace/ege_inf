f = open('24_aprobation2023_1.txt').readline()

file = f.replace('B', 'C')

for i in range(10000):
    if i*'CCA' in file:
        print(i*3) #<- ВЫВОДИМ ДЛИНУ ПОСЛЕДОВАТЕЛЬНОСТИ ТАКИХ ТРОЕК