# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = [[int(input("введите число: ")) for _ in range(5)] for _ in range(4)]

for line in matrix:
    sum_line = 0
    for el in line:
        sum_line += el
    c = line.append(f"  | {sum_line}")

for line in matrix:
    for el in line:
        print(f'{el:>4}', end='')
    print()
