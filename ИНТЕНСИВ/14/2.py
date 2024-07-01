for x1 in '0123456789ABCDE':
    for y1 in '0123456789ABCDE':
        s = int(f'90{x1}4{y1}', 15) + int(f'91{x1}{y1}2', 16)
        if s % 56 == 0:
            print(s // 56)
