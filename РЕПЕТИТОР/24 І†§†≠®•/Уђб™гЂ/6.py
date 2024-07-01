f = open('24_demo2022.txt').readline()


file = f.replace('PP', 'P P')
print('PP' not in file)

file = file.split()
print(len(max(file, key=len)))