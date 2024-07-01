P = [i for i in range(25, 51)]
Q = [i for i in range(32, 48)]
A = [i for i in range(25, 51)]

for x in range(25, 51):
    F = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
    if F == 1:
        A.remove(x)

print(A, max(A) - min(A))