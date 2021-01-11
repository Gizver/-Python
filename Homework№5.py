# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.


with open('text.txt', 'w') as f_obj:
    while True:
        string=input('Введите строку(Enter чтобы закончить): ')
        sf=f_obj.write(f'{string}\n')
        if not string:
            break


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


with open('text2.txt') as f_obj:
    i=1
    for el in f_obj:
        print(f'{len(el.split())} слов в {i} строке')
        i+=1
    print(f'Всего строк {i - 1}')


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
people={
    'Смирнов':25000,
    'Токарев':19000,
    'Злобов':33000,
    'Титов':15000
}
with open('text3.txt', 'w+') as f_obj:
    for key, val in people.items():
        f_obj.write(f'{key} : {val}\n')
    f_obj.seek(0)
    result=0
    for part in f_obj:
        a=part.split()
        for el in a:
            if el.isdigit():
                result+=int(el)
                if int(el)<20000:
                    print(a[0])
    print(f'Средний оклад {result}')

# 4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dictionary={
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('text4.txt', 'r+', encoding='utf-8' ) as f_obj:
    for el in f_obj:
        el=el.split()
        el[0] = dictionary[el[0]]
        print(el[0])
        with open('text5.txt', 'a', encoding='utf-8') as f1_obj:
            string=' '.join(el)
            f1_obj.writelines(f'{(string)}\n')

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

numbers='2 45 64 42 21 4 67'
with open('text6.txt', 'w+' ) as f_obj:
    result=0
    f_obj.write(numbers)
    f_obj.seek(0)
    for el in f_obj:
        el=el.split()
        for number in el:
            result+=int(number)
        print(f'Сумма всех чисел: {result}')

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести словарь на экран.

with open('text7.txt','r',encoding='utf-8') as f_obj:
    dictionary = {}
    result1=[]
    for el in f_obj:
        i = 0
        result = []
        while i<len(el):
            number = ''
            a=el[i]
            while a.isdigit():
                number+=a
                i+=1
                if i<len(el):
                    a=el[i]
                else:break
            i+=1
            if number !='':
                result.append(int(number))
        result1.append(sum(result))
    print(f' Список сумм часов по каждому предмету: {result1}')
    f_obj.seek(0)
    k = 0
    for el in f_obj:
        el=el.split()
        dictionary[el[0]]=result1[k]
        k+=1
    print(dictionary)


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json
with open('text8.txt','r', encoding='utf-8') as f_obj:
    result=[]
    average_profit_dict={}
    average_profit=[]
    dictionary={}
    for el in f_obj:
        el=el.split()
        profit=int(el[2])-int(el[3])
        dictionary[el[0]]=profit
        if profit>0:
            average_profit.append(profit)
    average_profit=sum(average_profit)
    average_profit_dict['average_profit']=average_profit
    result.append(dictionary)
    result.append(average_profit_dict)
    print(result)
    with open("my_file.json", "w") as write_f:
        json.dump(result, write_f)