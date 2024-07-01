f = open('24_ege2021.txt')
s = f.readline()

file = s.replace('ad', 'a d')
file = file.replace('da', 'd a')
file = file.split()

print(len(max(file, key=len)))