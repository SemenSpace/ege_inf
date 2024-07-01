n = 116 * "7"

while "333" in n or "7777" in n:
    if "333" in n:
        n = n.replace("333", "77", 1)
    else:
        n = n.replace("7777", "3", 1)

print(n)
