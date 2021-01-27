# Определить, какое число в массиве встречается чаще всего.

from random import randint

a = [randint(1, 10) for _ in range(20)]
print(a)
c = {x: 0 for x in list(set(a))}
for el in a:
    if el in a:
        c[el] += 1
print(c)
max = (0, 0)
for key, item in c.items():
    if item > max[1]:
        max = key, item
print(f"Чаще всего в массиве встречается число {max[0]}")
