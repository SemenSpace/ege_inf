f = open('10.txt')
n = int(f.readline())
f = sorted([int(i) for i in f], reverse=True)
proc_20 = int(n * 0.2)

mx_ind = 0
mx_razn = 0

for i in range(proc_20, len(f) - 1):
    razn = min(f[:i + 1]) - max(f[i + 1:])

    if mx_razn < razn:
        mx_razn = razn
        mx_ind = i
print(len(f[:mx_ind + 1]))
print(min(f[:mx_ind + 1]))
