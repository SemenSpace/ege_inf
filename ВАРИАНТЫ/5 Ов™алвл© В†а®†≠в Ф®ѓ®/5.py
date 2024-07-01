kon = []

for N in range(1, 1000):
    R = bin(N)[2:]
    if R[-1] == '0':
        R = '10' + R
    else:
        R = '1' + R + '01'
    print(int(R, 2), N)
    if int(R, 2) > 516:
        kon.append([N, int(R, 2)])

print(sorted(kon))