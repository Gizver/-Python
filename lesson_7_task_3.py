# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
# его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

# сортировка расческой

import random

size = 11
array = [random.randint(-100, 99) for i in range(size)]
print(array)


def comb(data):
    gap = len(data)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 2))
        swaps = False
        for i in range(len(data) - gap):
            j = i + gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                swaps = True
    return data


m = (len(array)) // 2
print(comb(array))
print(f'Медиана массива: {array[m]}')
