P = [i/10 for i in range(40, 151)]
Q = [i/10 for i in range(120, 201)]

A = []


for x in range(-5000, 5000):
    x /= 10
    if (((x in P) and (x in Q)) <= (x in A)) == 0:
        A.append(x)

print(max(A) - min(A))