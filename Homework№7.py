# 1 Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке. Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
list1 = [
    [17, 34, 72, 29],
    [52, 54, 26, 87],
    [82, 32, 98, 45],

]
list2 = [
    [170, 34, 72, 29],
    [520, 54, 26, 87],
    [820, 32, 98, 45]
]


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        __mat = ''
        for el in self.list:
            string = ''
            for num in el:
                string += f'{num} '
            __mat += f'{string}\n'
        return f'{__mat}'

    def __add__(self, other):
        add_list = []
        i = 0
        while i < len(self.list):
            new = list(map(lambda x, y: x + y, self.list[i], other.list[i]))
            add_list.append(new)
            i += 1
        return Matrix(add_list)


s = Matrix(list1)
b = Matrix(list2)
print(s + b)

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def material(self):
        pass

    def __add__(self, other):
        return f'Общий расход ткани: {self.material + other.material} м'

    def __str__(self):
        return f'Расход ткани на изделие: {self.material}'


class Coat(Clothes):
    @property
    def material(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def material(self):
        return round(2 * self.param + 0.3, 2)


c = Coat(10)
f = Costume(6)
print(c + f)
print(c)

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
from math import ceil


class Cell:
    def __init__(self, amount):
        if isinstance(amount, int):
            self.amount = amount
        else:
            raise TypeError

    def __str__(self):
        return f'{self.amount}'

    def __add__(self, other):
        self.amount = (self.amount + other.amount)
        return Cell(self.amount)

    def __sub__(self, other):
        self.amount=self.amount - other.amount
        return Cell(self.amount)

    def __mul__(self, other):
        self.amount=self.amount * other.amount
        return Cell(self.amount)

    def __truediv__(self, other):
        self.amount=round(self.amount / other.amount)
        return Cell(self.amount)

    def make_order(self, number_in_row):
        row_number = ceil(self.amount / number_in_row)
        a = ''
        for i in range(row_number):
            a += number_in_row * '*' + '\n'
        a += (self.amount % number_in_row) * '*'
        return a


x = Cell(14)
y = Cell(6)
print(x + y)
print(x)
print(x - y)
print(x * y)
print(x / y)
print((x - y).make_order(7))
