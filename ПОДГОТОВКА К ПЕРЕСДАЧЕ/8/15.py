from itertools import *

k=0
for i in permutations('ДЕЙКСТРА', r=6):
    s = ''.join(i)
    s = s.replace('К', 'Д').replace('С', 'Д').replace('Т', 'Д').replace('Р', 'Д')
    if i.count('Й') == 1:
        if 'ЙД' in s:
            k += 1
print(k)