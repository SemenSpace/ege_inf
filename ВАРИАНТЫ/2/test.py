n = ">" + "1" * 11 + "2" * 12 + "3" * 30

while ">1" in n or ">2" in n or ">3" in n:
    if ">1" in n:
        n = n.replace(">1", "22>", 1)
    if ">2" in n:
        n = n.replace(">2", "2>", 1)
    if ">3" in n:
        n = n.replace(">3", "1>", 1)

print(sum([int(i) for i in n[:-1]]))
