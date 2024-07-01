f = open('24_open_kim2023.txt').readline()

f = f.replace('A', '*')
f = f.replace('B', '*')
f = f.replace('C', '*')
f = f.replace('**', '* *')

f = f.split()
print(len(max(f, key=len)))
