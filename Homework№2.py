# # 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# # Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print('Задание 1')
list_type = ['Строка', 15, 15.15, (1, 2, 3), [4, 5, 6], {11, 43, 456, 777}, {'name': 'Stan', 'age': 26}, True, None,
             b"some text", bytearray(b"some text"), ZeroDivisionError]
print(list_type)
for el in list_type:
    print(type(el))

# # 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# # При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

print('Задание 2')
amount = int(input('Введите количество элементов: '))
list_for_2d = []
i = 0
while i < amount:
    i += 1
    element = input('Введите {}-й элемент: '.format(i))
    list_for_2d.append(element)

for i in range(0, amount - 1, 2):
    list_for_2d[i], list_for_2d[i + 1] = list_for_2d[i + 1], list_for_2d[i]
print(list_for_2d)

# # 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
print('Задание 3')
mounth = int(input('Введите месяц: '))

# # #Через list:

mounth_list = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
if mounth in mounth_list[0]:
    print('зима')
elif mounth in mounth_list[1]:
    print('весна')
elif mounth in mounth_list[2]:
    print('лето')
else:
    print('осень')
#
# # #Через dict:
#
mounth_list = {'зима': [1, 2, 3], 'весна': [4, 5, 6]}
for val in mounth_list:
    if mounth in mounth_list.values():
        print(mounth_list.values())
mounth_list = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето',
               9: 'осень', 10: 'осень', 11: 'осень'}
if mounth in mounth_list:
    print(mounth_list[mounth])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

print('Задание 4')
words = input('Введите слова через пробел: ')

words_list = list(words.split())
i = 0
while i < len(words_list):
    print(words_list[i][:10])
    i += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

print('Задание 5')
my_list = [8, 7, 6, 6, 4, 2]
print(my_list)
number = int(input('Введите число: '))
my_list.append(number)
my_list.sort()
my_list.reverse()
print(my_list)

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
print('Задание 6')
result = []
i = 1
while True:
    name = input('Название: ')
    cost = int(input('Цена: '))
    amount = int(input('Количество: '))
    unit = input('Единицы: ')
    list_new = []
    my_dict = {'название': name, 'Цена': cost, 'Количество': amount, 'Единицы': unit}
    list_new.append(i)
    list_new.append(my_dict)
    result.append(tuple(list_new))
    answer = input("Продолжить заполнение?(да/нет): ")
    i += 1
    if answer.lower() == 'да':
        continue
    else:
        break
print(result)

# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик

list1 = []
new_dict = dict(result)
for val in new_dict.values():
    x = val.values()
    list1.append(list(val.values()))

# создаю списки характеристик
i = 0
list_name = []
while i < len(list1):
    list_name.append(list1[i][0])
    i += 1

i = 0
list_cost = []
while i < len(list1):
    list_cost.append(list1[i][1])
    i += 1

i = 0
list_amount = []
while i < len(list1):
    list_amount.append(list1[i][2])
    i += 1

i = 0
list_unit = []
while i < len(list1):
    list_unit.append(list1[i][3])
    i += 1
list_unit = list(set(list_unit))  # перевод списка в множество

new_dict = {'название': list_name, 'цена': list_cost, 'количество': list_amount, 'ед': list_unit}
print(new_dict)
