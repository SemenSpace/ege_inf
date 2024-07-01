P = [i/10 for i in range(250, 501)]
Q = [i/10 for i in range(320, 471)]

A = []


for x in range(-5000, 5000):
    x /= 10
    if (((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))) == 1:
        A.append(x)

print(max(A) - min(A))