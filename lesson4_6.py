from itertools import count, cycle
count1 = count(1)
cycle1 = cycle("qwerty")
for i in range(6):
    print(next(count1), next(cycle1))

