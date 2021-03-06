# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию). Каждую задачу необходимо сохранять в отдельный файл.
# Рекомендуем использовать английские имена, например, les_6_task_1.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
#
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.

# Урок 2, Задание 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
import sys
import inspect

sys.setrecursionlimit(100000)

n = int(input('Введите длину ряда: '))


def gtszf(v):
    sz = sum(map(sys.getsizeof, v.values()))
    print('-' * 35, inspect.stack()[1][3], '-' * 35)
    print(f'Объем памяти, выделенный на все переменные в данном алгоритме занимает - {sz} байт.')
    return sz


def les_2_task_4(n):
    summ = 0
    for sqrt in range(n):
        summ += (-0.5) ** sqrt
    gtszf(locals())
    return summ


def rec(s_rec, n_rec):
    summ = s_rec
    if n_rec == 1:
        pass
    else:
        s1 = s_rec * (- 0.5)
        summ = s_rec + rec(s1, n_rec - 1)
    if n_rec == n:
        gtszf(locals())
    return summ


def series(n):
    s_arr = [1]
    for _ in range(1, n):
        s_arr.append(s_arr[-1] * (- 0.5))
    summ = sum(s_arr)
    gtszf(locals())
    return summ


def series_long(n):
    s_arr = [1]
    summ_arr = 0
    for _ in range(1, n):
        s_arr.append(s_arr[-1] * (- 0.5))
    for i in s_arr:
        summ_arr += i
    gtszf(locals())
    return summ_arr


print(f'Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = {n}, равна - {les_2_task_4(n)}\n')
print(f'Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = {n}, равна - {rec(1, n)}\n')
print(f'Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = {n}, равна - {series(n)}\n')
print(f'Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = {n}, равна - {series_long(n)}\n')



# Windows 10 x64, Python 3.6

# ----------------------------------- les_2_task_4 -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 44 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4, равна - 0.625
#
# ----------------------------------- rec -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 60 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4, равна - 0.625
#
# ----------------------------------- series -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 100 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4, равна - 0.625
#
# ----------------------------------- series_long -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 116 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4, равна - 0.625



# ----------------------------------- les_2_task_4 -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 44 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 400, равна - 0.6666666666666667
#
# ----------------------------------- rec -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 60 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 400, равна - 0.6666666666666666
#
# ----------------------------------- series -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 1732 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 400, равна - 0.6666666666666667
#
# ----------------------------------- series_long -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 1748 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 400, равна - 0.6666666666666667



# ----------------------------------- les_2_task_4 -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 44 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4000, равна - 0.6666666666666667
#
# ----------------------------------- rec -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 60 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4000, равна - 0.6666666666666667
#
# ----------------------------------- series -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 17356 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4000, равна - 0.6666666666666667
#
# ----------------------------------- series_long -----------------------------------
# Объем памяти, выделенный на все переменные в данном алгоритме занимает - 17372 байт.
# Сумма n элементов ряда чисел: 1, -0.5, 0.25, -0.125,… при n = 4000, равна - 0.6666666666666667



# функции series и series_long имеют большее потребление памяти в связи с записью всей последовательности чисел в массив
# с последующим сложением всех элементов массива. series_long немного больше ест памяти чем series
# из-за питоновского сложения в цикле с использованием временной переменной, а не использования встроенной функции sum
# rec имеет ограничения по глубине рекурсии, что является потенциальным ограничением для работы всего алгоритма
# les_2_task_4 - исходная функция из второго дз - не имеет ограничений функции rec и при этом потребляет меньше памяти
