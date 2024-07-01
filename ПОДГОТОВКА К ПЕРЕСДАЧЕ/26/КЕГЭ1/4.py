f = open('4.txt')
s, n = map(int, f.readline().split())
f = [int(i) for i in f]

mass = s

kon = []
for i in sorted(f):
    if s - i >= 0:
        s -= i
        n -= 1
        f.remove(i)
    else:
        break


print(n, sum(f))