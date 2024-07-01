n = "1" * 81

while "1111" in n or "88888" in n:
    if "1111" in n:
        n = n.replace("1111", "888", 1)
    else:
        n = n.replace("88888", "888", 1)


print(n)
