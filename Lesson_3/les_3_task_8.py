# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print('Матрица 5х4')

m_4x4 = [[int(num) for num in input(f'Введите 4 числа строки №{input_+1} через пробел:').split()] for input_ in
         range(4)]

for row_i, row in enumerate(m_4x4):
    s = 0
    for row_num in row:
        s += row_num
    m_4x4[row_i].append(s)

for row in m_4x4:
    for i in row:
        print(f'{i:<3}', end='')
    print()
