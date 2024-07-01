f = open('11.txt')
n = int(f.readline())
f = sorted([list(map(int, i.split())) for i in f])
f.remove([])
num_rid = 0
num_place = 0
kon = []
for i in range(len(f) - 1):
    r1, p1 = f[i]
    r2, p2 = f[i + 1]
    if r1 == r2:
        if r1 not in kon:
            if p2 - p1 == 3:
                kon.append(r1)
                num_rid = r1
                num_place = p1 + 1
                continue

print(num_rid, num_place)