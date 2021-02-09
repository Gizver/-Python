# Определить, какое число в массиве встречается чаще всего.

from random import randint
import sys
'''
Python 3.8.5
MSC v.1916 64 bit (AMD64)
win32
'''
'''
В данном примере, размер размер словаря может очень сильно превышать размер аналогичного списка,
в зависимости от количества уникальных элементов
'''
size=50
array=[randint(0, size//2) for _ in range(size)]

diction={ }
for item in array:
    if item in diction.keys():
        diction[item]+=1
    else:
        diction[item]=1

a=[]
for key, value in diction.items():
    a.append((key,value))
print(diction)
print(a)
print(sys.getsizeof(diction))
print(sys.getsizeof(a))