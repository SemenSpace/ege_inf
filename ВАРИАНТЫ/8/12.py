n = 82 * "8"

while "1111" in n or "8888" in n:
    if "1111" in n:
        n = n.replace("1111", "8", 1)
    else:
        n = n.replace("8888", "11", 1)

print(n)
