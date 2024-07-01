f = open('9.txt').readline()
f = f.replace('B', 'A')
f = f.replace('2', '1')
f = f.replace('11A', '*').replace('1', 'A').split('A')

print(len(max(f, key=len)))
print(max(f, key=len))