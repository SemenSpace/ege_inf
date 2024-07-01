

file = open('26.2.txt')
n = int(file.readline())
f = [list(map(int, i.split())) for i in file]
f.sort()

screen = ['0'*100001 for i in range(100001)]

for i in f:
    row, colomn = i
    screen[row] = screen[row][:colomn] + '1' + screen[row][colomn + 1:]

print(screen)