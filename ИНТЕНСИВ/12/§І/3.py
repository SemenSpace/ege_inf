n = "0" + 15 * "2" + 17 * "3" + 12 * "1"

while "01" in n or "02" in n or "03" in n:
    n = n.replace("01", "20", 1)
    n = n.replace("02", "120", 1)
    n = n.replace("03", "302", 1)

print(n.count('1'))