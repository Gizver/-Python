# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 12
numbers = [1, 2, 3, 4, 5]
example = 'Пример'
print(a)
print(example)
print(example, a)
print(numbers)
name = input('Ваше имя: ')
age = int(input('Ваш возраст: '))
print(f'Ваше имя {name}')
print(f'Вам {age} лет')


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input("Введите количество секунд: "))
h = seconds // 3600
m = (seconds - h * 3600) // 60
s = seconds - h * 3600 - m * 60
print('Ваши секунды в формате чч:мм:сс:')
print(f'{h}:{m}:{s}')


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n=input('Введите число:')
nn=n+n
nnn=nn+n
print('Сумма формата чисел в формате n + nn + nnn: ')
print(int(n)+int(nn)+int(nnn))


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.



a = int(input("Введите целое положительное число: "))
l = a % 10
a = a // 10
while a > 0:
    if l < a % 10:
        l = a % 10
    a = a // 10
print(l)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников
# фирмы и определите прибыль фирмы в расчете на одного сотрудника.

cash=int(input('Введите выручку: '))
cost = int(input('Введите издержки: '))
profit=cash-cost
if profit>cost:
    print(f'Фирма получает прибыль: {profit} у.е.')
    profitability=profit/cash
    print(f'Рентабельность выручки: {round(profitability,2)}')
    workers=int(input('Введите численность сотрудников: '))
    profitability_per_workers=profit/workers

    print(f'Прибыль в расчете на одного сотрудника {round(profitability_per_workers,2)} у.е.')
else:
    print('Фирма терпит убытки')


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составит не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.

a=int(input('Результат в первый день: '))
b=int(input('Конечный результат: '))
i=1
while a<b:
    i+=1
    a*=1.1

print(f'На {i}-й день спортсмен достиг результата — не менее {b} км')
