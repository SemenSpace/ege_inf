P = [i for i in range(5,31)]
Q = [i for i in range(14,24)]
A = [i for i in range(5,31)]


for x in range(5,31):

    if (((x in P) == (x in Q)) <= (not(x in A))) == 1:
        A.remove(x)

print(A)
print(max(A) - min(A))