kon = []
aplf = "0123456789ABCDEFGHI"
for x in aplf:
    s1 = int(f"98{x}79641", 19)
    s2 = int(f"36{x}14", 19)
    s3 = int(f"73{x}4", 19)
    s0 = s1 + s2 + s3
    if s0 % 18 == 0:
        kon.append([x, s0//18])

print(sorted(kon, reverse=True))
