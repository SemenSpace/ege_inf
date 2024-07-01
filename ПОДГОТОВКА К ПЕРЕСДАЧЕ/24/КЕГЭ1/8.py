f = open("8.txt").readline()
f = f.replace("C", "B").replace("D", "B")
f = f.replace("O", "A").replace('BA', '*').replace('B', 'A').split('A')

print(len(max(f, key=len)))