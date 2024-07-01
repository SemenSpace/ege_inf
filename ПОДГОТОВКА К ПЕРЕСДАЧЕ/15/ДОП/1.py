P = [i/10 for i in range(50, 301)]
Q = [i/10 for i in range(140, 231)]

A = [i/10 for i in range(50, 301)]


for x in range(50, 301):
    x /= 10
    if (((x in P) == (x in Q)) <= (not(x in A))) == 1:
        A.remove(x)

print(A)