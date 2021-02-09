# Найти два наименьших элемента массива
import sys, random

'''
Python 3.8.5
MSC v.1916 64 bit (AMD64)
win32
'''
'''
В данном примере, размер элемента списка будет 28 байт.
Размер списка может быть меньше, чем сумма всех его элементов, тк на один и тот же объект будет одинаковые ссылки.
'''
m = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {m}')

min_index_1 = 0
min_index_2 = 1

for i in m:
    if m[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = m.index(i)
    elif m[min_index_2] > i:
        min_index_2 = m.index(i)

print(f'Два наименьших элемента: {m[min_index_1]} и {m[min_index_2]}')
print('Размер списка', sys.getsizeof(m))
print('Размер элемента списка', sys.getsizeof(m[0]))
sum = 0
for size in m:
    sum += sys.getsizeof(size)
print('Размер всех элементов в листе', sum)

