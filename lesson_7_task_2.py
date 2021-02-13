# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(object):
    if len(object) < 2:
        return object

    middle = len(object) // 2
    left = object[:middle]
    right = object[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result


l = [random.randint(-10, 10) for _ in range(10)]
print(l)
print(merge_sort(l))
