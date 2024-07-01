file = open("26.txt")
lines = file.readlines()

n, m = map(int, lines[0].split())
array = list(map(int, lines[1:]))
array = sorted(array)

i = 0
current_sum = 0
last_elem = 0
ind_last = 0
count = 0

while array[i] <= 210:
    if array[i] >= 200 and current_sum + array[i] <= m:
        current_sum += array[i]
        last_elem = array[i]
        count += 1
    else:
        ind_last = i
    i += 1

for j in range(ind_last):
    if current_sum + array[j] <= m:
        current_sum += array[j]
        last_elem = array[j]
        count += 1

for j in range(i, len(array)):
    if current_sum + array[j] <= m:
        current_sum += array[j]
        last_elem = array[j]
        count += 1

free_space = m - current_sum + last_elem

for i in range(len(array) - 1, 0, -1):
    if array[i] <= free_space:
        current_sum += array[i] - last_elem
        break

print(count, current_sum)
