# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

N = int(input('Введите число: '))
my_list = []
for i in range(N):
    my_list.append(random.randint(1, 10))
print(my_list)

my_list_2 = []
if N % 2 == 0:
    for n in range(int(N/2)):
        my_list_2.append(my_list[n] * my_list[N-n-1])
else:
    for n in range(int(N/2+1)):
        my_list_2.append(my_list[n] * my_list[N-n-1])
print(my_list_2)