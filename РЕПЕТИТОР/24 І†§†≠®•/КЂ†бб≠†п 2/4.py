f = open('k7-m23.txt')
f = f.readline()

count = 0
cep = 0
for i in range(2, len(f)):
    if f[i] >= f[i - 1] >= f[i - 2]:
        count += 1
        cep = i - 2

print(count, cep)