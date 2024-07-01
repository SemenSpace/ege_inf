n = "3" + '9' * 93

while "19" in n or "299" in n or "3999" in n:
    n = n.replace("19", "2", 1)
    n = n.replace("299", "3", 1)
    n = n.replace("3999", "1", 1)

print(n)
