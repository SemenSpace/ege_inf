f = open('2.txt')
f = f.readline()
f = f.replace('2', '1').replace('3', '1').replace('B', 'A').replace('C', 'A').split('A')

print(len(max(f, key=len)))