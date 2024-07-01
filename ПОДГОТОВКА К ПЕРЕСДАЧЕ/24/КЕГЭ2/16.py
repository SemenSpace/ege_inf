f = open("16.txt").readline()
alp = sorted("qwertyuiopasdfghjklzxcvbnm".upper())

mx = 0
mn = 10**10
for i in alp:
    mx = max(mx, f.count(i))
    mn = min(mn, f.count(i))

print(mx - mn)
