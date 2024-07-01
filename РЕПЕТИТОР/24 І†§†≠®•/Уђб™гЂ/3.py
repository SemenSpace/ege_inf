f = open('24_aprobation2021.txt')
s = f.readline()

# ДЛИНА ВСЕХ СТРОК БЕЗ G W P
file = s.replace('G', ' ')
file = file.replace('W', ' ')
file = file.replace('P', ' ')

file = file.split()
print(len(max(file, key=len)))