# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = [[random.randint(1, 50) for _ in range(5)] for _ in range(4)]
for line in matrix:
    for el in line:
        print(f'{el:>4}', end='')
    print()

min_columns = [el for el in matrix[0]]
for line in matrix:
    for i, el in enumerate(line):
        if min_columns[i] > el:
            min_columns[i] = el
max_el = min_columns[0]
for el in (min_columns):
    if el > max_el:
        max_el = el
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_el}')
