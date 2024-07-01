f = open('27-B.txt')
k, n = int(f.readline()), int(f.readline())
f = [int(i) for i in f]

mx = 0
for i in range(2*k, n):
    s = f[i] + f[i - 2*k]
    if s > mx:
        mx  = s
        print(f[i], f[i - 2*k])
## 70146 55871 79689
print(sorted(f)[-1])

print(70146+55871+79689)
print(7958+7962+7974)



