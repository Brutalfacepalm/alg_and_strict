# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random
import numpy
import cProfile

# генератор списка Python
def gen_array(N):
    len_arr = N
    START_ELEM = 0
    END_ELEM = 100

    arr = [random.randint(START_ELEM, END_ELEM) for _ in range(len_arr)]

    return arr

# генератор списка numpy
def gen_array_numpy(N):
    len_arr = N
    START_ELEM = 0
    END_ELEM = 100

    arr = numpy.random.randint(START_ELEM, END_ELEM, len_arr)

    return arr

def search_min_hw(arr):
    min_arr = []

    for _ in range(2):
        min_i = 0
        min_num = arr[min_i]
        for i, item in enumerate(arr):
            if item <= min_num:
                min_num = item
                min_i = i
        min_arr.append(str(arr.pop(min_i)))

def search_min_opt(arr):
    END_ELEM = 100
    min_first = END_ELEM
    min_second = END_ELEM

    for i in arr:
        if i <= min_first:
            min_second = min_first
            min_first = i
        elif i <= min_second:
            min_second = i

def search_min_sort(arr):
    START_ELEM = 0
    END_ELEM = 100
    m = []
    for i in range(START_ELEM, END_ELEM+1):
        if i in arr:
            m.append(i)
            if arr.count(i) > 1:
                m = [i, i]
                break
            else:
                if len(m) == 2:
                    break

def search_min_def(arr):

    arr.sort()
    m = [arr[0], arr[1]]

def search_min_numpy(arr):

    m = arr.argsort()[:2:]

# "les_4_task_1.main_hw(500000)"
# 100 loops, best of 3: 799 msec per loop
# "les_4_task_1.main_hw(50000)"
# 100 loops, best of 3: 75.7 msec per loop
# "les_4_task_1.main_hw(5000)"
# 100 loops, best of 3: 7.66 msec per loop
# N=50000000
# 1    5.871    5.871    5.871    5.871 les_4_task_1.py:27(search_min_hw)
# 1    0.000    0.000  110.755  110.755 les_4_task_1.py:8(gen_array)
# 1    0.000    0.000  116.626  116.626 les_4_task_1.py:84(main_hw)
# Сложность - O(n)
def main_hw(N):
    arr = gen_array(N)
    search_min_hw(arr)

# "les_4_task_1.main_opt(500000)"
# 100 loops, best of 3: 772 msec per loop
# "les_4_task_1.main_opt(50000)"
# 100 loops, best of 3: 75.2 msec per loop
# "les_4_task_1.main_opt(5000)"
# 100 loops, best of 3: 7.46 msec per loop
# N=50000000
# 1    3.746    3.746    3.746    3.746 les_4_task_1.py:39(search_min_opt)
# 1    0.000    0.000  111.650  111.650 les_4_task_1.py:8(gen_array)
# 1    0.000    0.000  115.396  115.396 les_4_task_1.py:98(main_opt)
# Сложность - O(n)
def main_opt(N):
    arr = gen_array(N)
    search_min_opt(arr)

# "les_4_task_1.main_sort(500000)"
# 100 loops, best of 3: 731 msec per loop
# "les_4_task_1.main_sort(50000)"
# 100 loops, best of 3: 70.7 msec per loop
# "les_4_task_1.main_sort(5000)"
# 100 loops, best of 3: 7.09 msec per loop
# N=50000000
# 1    0.000    0.000    0.663    0.663 les_4_task_1.py:51(search_min_sort)
# 1    0.000    0.000  110.240  110.240 les_4_task_1.py:8(gen_array)
# 1    0.000    0.000  110.903  110.903 les_4_task_1.py:111(main_sort)
# Сложность - O(n)
def main_sort(N):
    arr = gen_array(N)
    search_min_sort(arr)

# "les_4_task_1.main_def_c(500000)"
# 100 loops, best of 3: 859 msec per loop
# "les_4_task_1.main_def_c(50000)"
# 100 loops, best of 3: 83.5 msec per loop
# "les_4_task_1.main_def_c(5000)"
# 100 loops, best of 3: 8.21 msec per loop
# N=50000000
# 1    0.000    0.000   12.617   12.617 les_4_task_1.py:66(search_min_def)
# 1    0.000    0.000  110.009  110.009 les_4_task_1.py:8(gen_array)
# 1    0.000    0.000  122.626  122.626 les_4_task_1.py:126(main_def_c)
# Сложность - O(n)
def main_def_c(N):
    arr = gen_array(N)
    search_min_def(arr)

# "les_4_task_1.main_numpy(500000)"
# 100 loops, best of 3: 28.3 msec per loop
# "les_4_task_1.main_numpy(50000)"
# 100 loops, best of 3: 2.59 msec per loop
# "les_4_task_1.main_numpy(5000)"
# 100 loops, best of 3: 230 usec per loop
# N=50000000
# 1    0.000    0.000    5.248    5.248 les_4_task_1.py:72(search_min_numpy)
# 1    0.000    0.000    0.582    0.582 les_4_task_1.py:18(gen_array_numpy)
# 1    0.018    0.018    5.847    5.847 les_4_task_1.py:140(main_numpy)
# Сложность - O(n)
def main_numpy(N):
    arr = gen_array_numpy(N)
    search_min_numpy(arr)

# Вариант с функцией main_sort оказался самым быстрым из всех, за исключением, конечно, использования Numpy,
# но там скорость работы высокая из-за скорости генерации списка.
# Скорость работы обусловена тем, что вероятное минимально значение определено заранее,
# и проверяется только наличие этого минимального значения в исходном списке.
# Сочитание тех фактов, что в списке количество возможных значение (0-100) было значительно меньше длины списка(>=5000)
# и вероятность нахождения минимального значения в списке в самом начале работы цикла была высока.
# При увеличении диапазона чисел (0-1000000) в списке длиной 5000 приводит к ухудшению показателей работы многократно.
# диапазон чисел 0-1000000, N = 5000
# "les_4_task_1.main_hw(5000)"
# 100 loops, best of 5: 9.14 msec per loop
# "les_4_task_1.main_opt(5000)"
# 100 loops, best of 5: 8.8 msec per loop
# "les_4_task_1.main_sort(5000)"
# 100 loops, best of 5: 35.4 msec per loop
# "les_4_task_1.main_def_c(5000)"
# 100 loops, best of 5: 9.85 msec per loop
# "les_4_task_1.main_numpy(5000)"
# 100 loops, best of 5: 306 usec per loop
# результаты cProfile с диапазоном чисел: 0-1000000000 и N=5000000 (N в 10 раз меньше чем на тестах при диапазоне 0-100, т.к. система упала в MemoryError)
# 1    0.772    0.772    0.777    0.777 les_4_task_1.py:35(search_min_hw)

# 1    0.583    0.583    0.583    0.583 les_4_task_1.py:47(search_min_opt)

# 1   23.480   23.480   23.646   23.646 les_4_task_1.py:59(search_min_sort)

# 1    0.000    0.000    6.021    6.021 les_4_task_1.py:73(search_min_def)

# 1    0.000    0.000    1.416    1.416 les_4_task_1.py:78(search_min_numpy)

# В связи с этими тестами можно сказать, что, без использования сторонних библиотек, среди этих алгоритмов наиболее оптимальной оказалась
# функция main_opt, так как показывает стабильно высокую работу на всех диапазонах чисел