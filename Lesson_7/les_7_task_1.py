# 1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def gen_arr():
    LEN_ARRAY = 20000
    MIN_NUM = -100
    MAX_NUM = 99
    array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(LEN_ARRAY)]
    print(array)
    return array


def bubble(a):
    a.append(-100) # расширяем исходный массив для дальнейшей работы с ним
    for _ in a:
        rep = 0 # счетчик изменений массива
        for j in range(1, len(a) - 1, 2): # проходим массив с шагом 2
            if a[j] < a[j + 1]: # сверяем текущий элемент со следущим
                a[j], a[j + 1] = a[j + 1], a[j]
                rep = 1
            if a[j] > a[j - 1]: # сверяем текущий элемент с предыдущим
                a[j], a[j - 1] = a[j - 1], a[j]
                rep = 1
        if not rep: # если массив не изменился за проход - значит он отсортирован и выходим из цикла
            break
    a.pop() # удаляем добавленный для работы элемент в массив
    return a

print(bubble(gen_arr()))

# LEN_ARRAY = 20
# "from les_7_task_1 import bubble, gen_arr" "bubble(gen_arr())"
# 10000 loops, best of 3: 81.7 usec per loop

# LEN_ARRAY = 200
# "from les_7_task_1 import bubble, gen_arr" "bubble(gen_arr())"
# 100 loops, best of 3: 5.19 msec per loop

# LEN_ARRAY = 2000
# "from les_7_task_1 import bubble, gen_arr" "bubble(gen_arr())"
# 10 loops, best of 3: 490 msec per loop
