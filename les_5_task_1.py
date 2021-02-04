# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

amount = int(input('Введите количество предприятий: '))
base_company = {}
Company = namedtuple('Company', ['p1', 'p2', 'p3', 'p4'])
for i in range(amount):
    name = input(f'Введите название {i + 1}-го предприятия: ')
    profit1 = int(input('Прибыль за 1-й квартал: '))
    profit2 = int(input('Прибыль за 2-й квартал: '))
    profit3 = int(input('Прибыль за 3-й квартал: '))
    profit4 = int(input('Прибыль за 4-й квартал: '))
    base_company[name] = Company(profit1, profit2, profit3, profit4)

total_profit  = ()
for profit in base_company.values():
    total_profit += profit
avg_profit_total = sum(total_profit) / len(base_company)

for name, profit in base_company.items():
    if sum(profit) > avg_profit_total:
        print(f'Прибыль {name} больше средней')
    elif sum(profit) < avg_profit_total:
        print(f'Прибыль {name} меньше средней')
