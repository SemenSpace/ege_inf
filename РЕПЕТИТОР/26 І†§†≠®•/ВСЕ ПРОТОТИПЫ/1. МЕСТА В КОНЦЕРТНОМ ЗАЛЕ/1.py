f = open('26_1.txt')
kol = int(f.readline())
file = [i.split() for i in f]

file.sort()
kon = []
for i in range(kol - 1):
    if file[i][0] == file[i + 1][0]:
        if abs(int(file[i][1]) - int(file[i + 1][1])) == 3:
            kon.append(file[i])

print(kon)