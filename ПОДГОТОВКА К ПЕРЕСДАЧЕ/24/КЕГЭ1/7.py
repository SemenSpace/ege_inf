f = open("7.txt").readline().replace("NPO", "*").replace("PNO", "*").replace('\n', 'O').replace('N', 'O').replace('P', 'O').split('O')

print(f)
print(len(max(f, key=len)))
