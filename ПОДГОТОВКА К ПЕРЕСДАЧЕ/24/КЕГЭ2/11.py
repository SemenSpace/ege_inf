f = open('11.txt')
f = [str(i) for i in f]
k = 0

for i in f:
    for j in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        if str(f'K{j}GE') in i:
            k += 1
            break
print(k)