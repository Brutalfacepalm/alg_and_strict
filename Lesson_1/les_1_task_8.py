# Определить, является ли год, который ввел пользователь, високосным или не високосным.
y = int(input('Введите год: '))
if y % 4 == 0:
    print('Год високосный.')
else:
    print('Год невисокосный.')