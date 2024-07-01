from itertools import *

k = 0
for a in '12345678':
    for b in '012345678':
        for c in '012345678':
            for d in '012345678':
                for e in '012345678':
                    if a > b > c > d > e:
                        k += 1


print(k)


from itertools import product
cnt = 0
for x in product('012345678', repeat=5):
    q = ''.join(x)
    if int(q[0]) > int(q[1]) > int(q[2]) > int(q[3]) > int(q[4]):
        cnt += 1
print(cnt)