# 3 Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random
from collections import deque
import cProfile

# генератор массива
def gen_arr():
    len_array = 2 * int(input('Введите длину массива: ')) + 1
    MIN_NUM = -100
    MAX_NUM = 100
    array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(len_array)]
    return array

# поиск мидианы без сортировки
def non_sort(arr):
    up_mid = []
    down_mid = []

    mid_v = sum(arr) / len(arr) # находим среднее значение

    for i in arr: # разрез массива по среднему значению
        if i > mid_v:
            up_mid.append(i)
        else:
            down_mid.append(i)

    while True: # цикл работает пока стороны вокруг среднего значения не уравняются, буквально так мы ищем и актуализируем среднее значение
        if len(up_mid) > len(down_mid):
            i = up_mid.pop(up_mid.index(min(up_mid)))
            if len(up_mid) == len(down_mid):
                break
            else:
                down_mid.append(i)
        else:
            i = down_mid.pop(down_mid.index(max(down_mid)))
            if len(up_mid) == len(down_mid):
                break
            else:
                up_mid.append(i)
    return i


# поиск мидианы стандартным способом: отсортировать и взять элеммент из середины списка
# ваще сделал для проверки
def s(arr):
    arr = sorted(arr)
    i = arr[len(arr) // 2]
    return i

# тут длинная и,судя по результатам - кривая, реализации сортировки TimSort,
# что называется - не стреляйте в пианиста, играет как умеет
# описание алгоритма взял с хабра https://habr.com/ru/company/infopulse/blog/133303/
# реализовывал как было понято из описания
# оптимизацией не особо занимался, не хватило времени

# поиск минимальной длины подмассива
def _minrun(arr):
    n = len(arr)
    r = 0
    while n >= 64:
        r = 0 | n & 1
        n = n >> 1

    minrun = n + r
    return minrun

# начинаем формировать подмассивы
def _get_runs(arr, minrun):
    runs_in_arr = []
    run = deque()
    flag = ''
    i = 1
    while i < len(arr):
        if flag == '':
            if arr[i - 1] <= arr[i]:
                flag = 'up'
            else:
                flag = 'down'
        else:
            if flag == 'up':
                if arr[i - 1] <= arr[i]:
                    run.append(arr[i - 1])
                    i += 1
                    continue
                else:
                    flag, run, i, runs_in_arr = _set_to_run(flag, arr, run, minrun, i, runs_in_arr)

            if flag == 'down':
                if arr[i - 1] > arr[i]:
                    run.appendleft(arr[i - 1])
                    i += 1
                    continue
                else:
                    flag, run, i, runs_in_arr = _set_to_run(flag, arr, run, minrun, i, runs_in_arr)

        run.clear()

    return runs_in_arr

# заканчиваем формировать подмассивы
def _set_to_run(flag, arr, run, minrun, i, runs_in_arr):
    if flag == 'up':
        run.append(arr[i - 1])
    elif flag == 'down':
        run.appendleft(arr[i - 1])
    if len(run) <= minrun:
        r = minrun - len(run) + 1
        if i + r < len(arr):
            run.extend(arr[i:i + r])
            i += r + 1
        else:
            run.extend(arr[i:])
            i += r + 1
        run = _insert_sort_run(run)

        runs_in_arr.append(list(run))
    else:
        i += 1
        run = _insert_sort_run(run)
        runs_in_arr.append(list(run))
    flag = ''

    return flag, run, i, runs_in_arr

# наконец сортируем подмассивы вставкой
# пробовал различные методы алгоритма(бинарный и парная вставка), но или запутывался(парная) или улучшения результата не увидел(бинарная)
def _insert_sort_run(run): # медленно работает сортировка
    for i in range(len(run)):
        for j in range(i + 1, len(run)):
            if run[i] > run[j]:
                run[i], run[j] = run[j], run[i]
    return run

# слияние подмассивов, недолго думая взял слияние из задания 2, модификацию не сделал, не хватило времени, да и вообще
def _merge(a):
    while len(a) > 1:
        for i in range(len(a) // 2):
            b = a.pop(i + 1)
            a[i] = _sort_m(a[i], b)
    return a[0]


def _sort_m(a, b): # почему то тоже работает сильно медленно
    s = []
    STOP = len(a) + len(b)
    a = list(a)
    b = list(b)
    while len(s) < STOP:
        if a and b:
            if a[0] < b[0]:
                s.append(a.pop(0))
            else:
                s.append(b.pop(0))
        else:
            if b:
                s.extend(b)
            else:
                s.extend(a)
    return deque(s)

# тут получаем отсортированный массив
def _timsort(arr):
    minrun = _minrun(arr)
    arr_runs = _get_runs(arr, minrun)
    arr_runs = _merge(arr_runs)
    return arr_runs

# по аналогии с s(arr): отсортировать и взять элеммент из середины списка
def mid_timsort(arr):
    sorted_arr = _timsort(arr)
    i = sorted_arr[len(sorted_arr) // 2]
    return i

arr = gen_arr()
arr_timsort = arr.copy()
arr_s = arr.copy()
arr_non_sort = arr.copy()


print('Сортировка TimSort: ', mid_timsort(arr_timsort))
print('Сортировка sorted: ', s(arr_s))
print('Поиск медианы без сортировки: ', non_sort(arr_non_sort))

# простая проверка с s(arr_s)

# len_array = 2 * 10 + 1
# "from les_7_task_3 import s, arr_s" "s(arr_s)"
# 1000000 loops, best of 3: 1.68 usec per loop

# len_array = 2 * 100 + 1
# "from les_7_task_3 import s, arr_s" "s(arr_s)"
# 10000 loops, best of 3: 31.7 usec per loop

# len_array = 2 * 1000 + 1
# "from les_7_task_3 import s, arr_s" "s(arr_s)"
# 10000 loops, best of 3: 466 usec per loop

# len_array = 2 * 10000 + 1
# "from les_7_task_3 import s, arr_s" "s(arr_s)"
# 1000 loops, best of 3: 5.32 msec per loop


# проверка с non_sort(arr_non_sort)

# len_array = 2 * 10 + 1
# "from les_7_task_3 import non_sort, arr_non_sort" "non_sort(arr_non_sort)"
# 1000000 loops, best of 3: 4.84 usec per loop

# len_array = 2 * 100 + 1
# "from les_7_task_3 import non_sort, arr_non_sort" "non_sort(arr_non_sort)"
# 10000 loops, best of 3: 54.1 usec per loop

# len_array = 2 * 1000 + 1
# "from les_7_task_3 import non_sort, arr_non_sort" "non_sort(arr_non_sort)"
# 10000 loops, best of 3: 409 usec per loop

# len_array = 2 * 10000 + 1
# "from les_7_task_3 import non_sort, arr_non_sort" "non_sort(arr_non_sort)"
# 1000 loops, best of 3: 3.77 msec per loop


# проверка с mid_timsort(arr_timsort)

# len_array = 2 * 10 + 1
# "from les_7_task_3 import mid_timsort, arr_timsort" "mid_timsort(arr_timsort)"
# 1000000 loops, best of 3: 47.8 usec per loop

# len_array = 2 * 100 + 1
# "from les_7_task_3 import mid_timsort, arr_timsort" "mid_timsort(arr_timsort)"
# 10000 loops, best of 3: 1.11 msec per loop

# len_array = 2 * 1000 + 1
# "from les_7_task_3 import mid_timsort, arr_timsort" "mid_timsort(arr_timsort)"
# 1000 loops, best of 3: 16.3 msec per loop

# len_array = 2 * 10000 + 1
# "from les_7_task_3 import mid_timsort, arr_timsort" "mid_timsort(arr_timsort)"
# 1000 loops, best of 3: 175 msec per loop


# print(cProfile.run('mid_timsort(arr_timsort)'))
# 567413 function calls in 0.287 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.287    0.287 <string>:1(<module>)
#       500    0.002    0.000    0.081    0.000 les_7_task_3.py:104(_set_to_run)
# ----------------------------------------------------------------------------------
#       500    0.077    0.000    0.079    0.000 les_7_task_3.py:129(_insert_sort_run) - самая простая сортировка вставками каждый подмассив
# ----------------------------------------------------------------------------------
#         1    0.001    0.001    0.204    0.204 les_7_task_3.py:138(_merge)
# ----------------------------------------------------------------------------------
#       499    0.122    0.000    0.203    0.000 les_7_task_3.py:149(_sort_m) - сортировка при слиянии
# ----------------------------------------------------------------------------------
#         1    0.000    0.000    0.287    0.287 les_7_task_3.py:169(_timsort)
#         1    0.000    0.000    0.287    0.287 les_7_task_3.py:176(mid_timsort)
#         1    0.000    0.000    0.000    0.000 les_7_task_3.py:60(_minrun)
#         1    0.002    0.002    0.083    0.083 les_7_task_3.py:71(_get_runs)