f = open('24_aprobation2023_3.txt').readline()

f = f.replace('N', '*')
f = f.replace('P', '*')
f = f.replace('O', '*')

f = f.replace('**', '* *')
f = f.replace('**', '* *')
f = f.replace('**', '* *')
f = f.replace('**', '* *')


f = f.split()
print(len(max(f, key=len)))
