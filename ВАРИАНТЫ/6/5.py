kon = []
for i in range(1000, 10000):
    s0 = []
    i = str(i)
    s1 = int(i[0]) + int(i[1])
    s2 = int(i[1]) + int(i[2])
    s3 = int(i[2]) + int(i[3])
    s0 = [s1, s2, s3]
    s0.sort(reverse=True)
    r = str(s0[1]) + str(s0[0])
    print(i, r)
    if int(r) == 613:
        kon.append([i, r])

print(sorted(kon))
