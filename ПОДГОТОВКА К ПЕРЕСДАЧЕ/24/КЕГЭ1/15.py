f = open('15.txt').readline()

kon = [0]*len(f)

for i in range(1, len(f)):
    if f[i - 1] + f[i] == 'BB' or f[i - 1] + f[i] == 'DD':
        kon[i] = kon[i - 2] + 1

print(max(kon))