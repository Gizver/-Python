# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import time


class Date:

    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def output(cls, self):
        date = list(map(int, self.dmy.split('-')))
        return date

    @staticmethod
    def validation(date):
        try:
            time.strptime(date, '%m-%d-%Y')
        except ValueError:
            print('Введена неверная дата!')


d = Date('12-12-2021')
print(Date.output(d))
Date.validation('11-12-2021')
Date.validation('12-12-2021')


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnExept(Exception):
    def __init__(self, text):
        self.text = text


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise OwnExept('Делитель не может быть равен нулю! ')
except OwnExept as error:
    print(error)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.

class OwnExept(ValueError):
    def __init__(self, text):
        self.text = text


list = []
while True:
    try:
        element = input('Введите число: ')
        if element.lower() == 'stop':
            break
        if not element.isdigit():
            raise OwnExept('Нужно вводить числа!')
        list.append(int(element))
    except OwnExept as er:
        print(er)
print(list)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.

class Storage:
    printers = []
    scanners = []
    copiers = []


class OwnExept(ValueError):
    def __init__(self, text):
        self.text = text


class Office_equipment:
    def __init__(self, name, number, price):
        self.name = name
        self.price = (price)
        self.number = (number)
        try:
            if isinstance(self.price, str) or isinstance(self.number, str):
                raise OwnExept(f'Для {self.name} - количество и цену нужно записать числами!')
        except OwnExept as er:
            print(er)
        self.info = {
            'модель': self.name,
            'цена': self.price,
            'количество': self.number
        }

    def __str__(self):
        return f'{self.info}'

    def shipment(self):
        Storage.printers.append(self.info)


class Printer(Office_equipment):
    def main_function(self):
        return 'Печать заданной информации'

    def shipment(self):
        Storage.printers.append(self.info)


class Scanner(Office_equipment):
    def main_function(self):
        return 'Сохранение графической информации в электронном виде'

    def shipment(self):
        Storage.scanners.append(self.info)


class Copier(Office_equipment):
    def main_function(self):
        return 'Делать ксерокопии'

    def shipment(self):
        Storage.copiers.append(self.info)


a = Printer('canon', 5, 5000)
b = Printer('HP', 2, 4500)
f = Scanner('canon', 4, 4000)
r = Copier('xerox', 6, 4599)
s = Storage
a.shipment()
b.shipment()
f.shipment()
r.shipment()

print(s.printers)
print(s.copiers)
print(s.scanners)


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'z={self.a}+{self.b}*i'

    def __add__(self, other):
        return f'z={self.a + other.a}+{self.b + other.b}*i'

    def __mul__(self, other):
        return f'z={self.a * other.a - self.b * other.b}+{self.a * other.b + self.b * other.a}*i'


first = ComplexNumber(1, -1)
second = ComplexNumber(3, 6)
print(first + second)
print(first * second)
