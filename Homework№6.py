# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        s = 0
        while s < 3:
            print(TrafficLight.__color[s])
            if s == 0:
                time.sleep(7)
            elif s == 1:
                time.sleep(2)
            else:
                time.sleep(7)
            s += 1


a = TrafficLight()
a.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, mass_cm, thickness):
        self._mass_cm = mass_cm
        self._thickness = thickness
        mass = self._length * self._width * mass_cm * thickness / 1000
        return f'Масса всего асфальта: {mass} т'


a = Road(1000, 50)
print(a.mass(10, 2))


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


a = Position('Krieg', 'Moll', 'manager', 10000, 4000)
print(a.get_full_name())
print(a.get_total_income())


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула на{direction}')

    def show_speed(self):
        print(f'скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    limit_speed = 60

    def show_speed(self):
        if self.speed > TownCar.limit_speed:
            print(f'Превышение скорости! Разрешенная скорость 60 км/ч. Текущая скорость автомобиля {self.speed} км/ч.')
        else:
            print(f'скорость автомобиля {self.speed} км/ч')


class WorkCar(Car):
    limit_speed = 40

    def show_speed(self):
        if self.speed > WorkCar.limit_speed:
            print(f'Превышение скорости! Разрешенная скорость 60 км/ч. Текущая скорость автомобиля {self.speed} км/ч.')
        else:
            print(f'скорость автомобиля {self.speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


a = TownCar(70, 'синий', 'Лексус')
a.go()
a.stop()
a.turn('право')
a.show_speed()
b = WorkCar(40, 'серый', 'Лексус')
b.show_speed()
c = SportCar(90, 'красный', 'Лексус')
c.go()
c.show_speed()
p = PoliceCar(80, 'черный', 'Лексус')
print(p.speed)
print(p.is_police)


# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашем')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


a = Stationery('мелок')
b = Pen('Гелевая ручка')
c = Pencil('Карандаш 2H')
d = Handle('Красный маркер')
print(a.title)
a.draw()
b.draw()
c.draw()
d.draw()
