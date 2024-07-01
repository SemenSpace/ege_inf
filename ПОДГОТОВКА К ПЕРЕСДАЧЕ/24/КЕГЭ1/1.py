f = open('1.txt')
f = f.readline()
f = f.replace('B', 'A').replace('E', 'A').replace('F', 'A')
f = f.replace('D', 'C').split('C')

print(len(max(f, key=len)))
