import math
for N in range(1, 2000):
    i = int(math.log(N, 2))
    if float(i) < math.log(N, 2):
        i += 1
    s = (42 + i)/8
    if float((42 + i)//8) < s:
        s = int(s) + 1
    if float((42 + i)//8) == s:
        s = int(s)

    if (N*s) == 2940:
        print(N)