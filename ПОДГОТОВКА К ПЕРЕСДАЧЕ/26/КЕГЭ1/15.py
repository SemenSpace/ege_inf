f = open('15.txt')
n, m = map(int, f.readline().split())
f = [[i.split()[0], int(i.split()[1])] for i in f]