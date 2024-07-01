f = open('14.txt').readline().strip()
kon = [1]*len(f)

for i in range(1, len(f)):
    if f[i] < f[i - 1]:
        kon[i] = kon[i - 1] + 1

for i in range(len(f)):
    if kon[i] == 8:
        print(f[i-7 : i + 1])