print('x y z w   f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = int(((y <= w) == (x <= (not(z)))) and (x or w))
                print(x, y, z, w, ' ', f)
