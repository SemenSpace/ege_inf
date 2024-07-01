a = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for p in range(10, 36 + 1):
    for x in a[:p]:
        for y in a[:p]:
            s1 = int(f'{x}{x}{x}8', p)
            s2 = int(f'43{x}9', p)
            s3 = int(f'{y}{y}04', p)
            if s1 + s2 == s3:
                print(int(f'{y}{y}{x}', p))