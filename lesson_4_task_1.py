# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…

import timeit, cProfile


def row1(n):
    a = 1
    sum = 0
    for i in range(n):
        sum += a
        a /= -2
    return sum


# lesson_4_task_1.row1(100)   :  1000 loops, best of 5: 13 usec per loop
# lesson_4_task_1.row1(10000) :  1000 loops, best of 5: 1.36 msec per loop
# lesson_4_task_1.row1(100000):  1000 loops, best of 5: 13.6 msec per loop


cProfile.run("row1(100000)")


# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#         1    0.016    0.016    0.016    0.016 lesson_4_task_1.py:4(row1)
#         1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def row2(n):
    return (((-0.5) ** n) - 1) / -1.5


# "lesson_4_task_1.row2(100)"   : 1000 loops, best of 5: 352 nsec per loop
# "lesson_4_task_1.row2(10000)" : 1000 loops, best of 5: 431 nsec per loop
# lesson_4_task_1.row2(100000)" : 1000 loops, best of 5: 443 nsec per loop

cProfile.run("row2(100000)")


# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:17(row2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def row3(n):
    return 1 + sum([1 * (-0.5) ** (i) for i in range(1, n)])


# "lesson_4_task_1.row3(100)"   : 1000 loops, best of 5: 28.6 usec per loop
# "lesson_4_task_1.row3(10000)" : 1000 loops, best of 5: 3.48 msec per loop
# "lesson_4_task_1.row3(100000)": 1000 loops, best of 5: 36.4 msec per loop

cProfile.run("row3(100000)")
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.035    0.035 <string>:1(<module>)
#         1    0.001    0.001    0.035    0.035 lesson_4_task_1.py:25(row3)
#         1    0.034    0.034    0.034    0.034 lesson_4_task_1.py:26(<listcomp>)
#         1    0.000    0.000    0.035    0.035 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Вывод. Как мы видим, row2 является предпочтительным вариантом, тк мы знаем формулу суммы геометрической последовательности.
# Без знания формулы, row1 будет работать быстрее row3, тк создание списка и его суммирование, занимает намного больше времени,
# чем вычисление следующего члена прогрессии и его суммирование
