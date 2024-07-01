P = [i/10 for i in range(200,501)]
Q = [i/10 for i in range(300, 651)]

A = []


for x in range(-5000, 5000):
    x /= 10
    print(x)
    if ((not(x in A)) <= ((x in P) <= (not(x in Q)))) == 0:
        A.append(x)

print(max(A) - min(A))