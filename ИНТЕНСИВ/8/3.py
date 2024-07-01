from itertools import *

k = 0
for i in set(permutations("ПАРАБОЛА")):
    s = str(''.join(i))
    s = s.replace("О", "А").replace("Р", "П").replace("Б", "П").replace("Л", "П")
    if ('ПП' not in i) and ('АА' not in s):
        k += 1


print(k)
