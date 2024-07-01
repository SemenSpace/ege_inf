kon = []
for x in range(0, 15):
    for y in range(0, 15):
        n = int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)
        if n % 56 == 0:
            kon.append(n // 56)

print(min(kon))