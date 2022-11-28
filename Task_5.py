# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibb(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)

num = int(input('Введите число: '))
my_list = [0]
for i in range(1, num + 1):
    my_list.append(fibb(i))
    if i % 2 != 0:
        my_list.insert(0, fibb(i))
    else:
        my_list.insert(0, -fibb(i))
print(my_list)
