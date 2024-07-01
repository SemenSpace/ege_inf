f = open("5.txt")
abitur, budget = map(int, f.readline().split())
f = [int(i) for i in f]

kon = []
last = 0
for i in sorted(f, reverse=True):
    if budget > 0:
        budget -= 1
        last = i
        kon.append(i)
    if budget == 0:
        break

k = 0
l = 0
for i in f:
    if kon[-1] == i:
        k += 1
    if k > 1:
        l = kon[-1]
        print(kon[-1])
        break

ne_postup = []
for i in f:
    if i not in kon:
        ne_postup.append(i)
mn = 10**10
for i in kon:
    if i != l:
        mn = min(mn, i)

print(mn, sum(ne_postup)/len(ne_postup))