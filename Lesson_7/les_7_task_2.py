# 2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def gen_arr():
    LEN_ARRAY = 200
    MAX_NUM = 50  # основание элементов массива
    # генерируем элементы массива в пределах [0;1)
    # и умножаем на основание
    array = [(random.random() * MAX_NUM) for _ in range(LEN_ARRAY)]
    print(array)
    return array


def merge(a):  # Слияние
    a = [[i] for i in a]  # Разделение массива на отсортированные массивы по 1 элементу
    while len(a) > 1:  # пока все не сольем в 1 элемент
        for i in range(len(a) // 2):  # //2 потому что на каждом шаге работает pop
            # для того чтобы из двух элементов получить один отсортированный в исходном массиве,
            # выдернем второй элемент на каждом шаге
            b = a.pop(i + 1)
            a[i] = sort_m(a[i], b) # отправляем массивы на слияние и сортировку
    # как итог вернем единственный отсортированный массив из массива
    return a[0]


def sort_m(a, b):
    s = []
    STOP = len(a) + len(b)
    while len(s) < STOP: # критерий остановки - пока мы не задействуем все элементы двух массивов
        if a and b: # пока оба массива существуют сравниваем их наименьшие элементы и затем выдергиваем меньший
            if a[0] < b[0]:
                s.append(a.pop(0))
            else:
                s.append(b.pop(0))
        elif a or b: # если какой то массив кончился, значит меньший элемент другого оказался
            # больше большего элемента первого и посему кидаем оставшийся массив в конец к результату
            if b:
                s.extend(b)
            else:
                s.extend(a)
    return s


print(merge(gen_arr()))

# LEN_ARRAY = 20
# "from les_7_task_2 import merge, gen_arr" "merge(gen_arr())"
# 5000 loops, best of 5: 57.2 usec per loop

# LEN_ARRAY = 200
# "from les_7_task_2 import merge, gen_arr" "merge(gen_arr())"
# 500 loops, best of 5: 825 usec per loop

# LEN_ARRAY = 2000
# "from les_7_task_2 import merge, gen_arr" "merge(gen_arr())"
# 20 loops, best of 5: 11.3 msec per loop

# LEN_ARRAY = 20000
# "from les_7_task_2 import merge, gen_arr" "merge(gen_arr())"
# 2 loops, best of 5: 178 msec per loop