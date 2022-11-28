# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

N = int(input('Введите число: '))
numbers = []
for i in range(N):
    if i % 3 == 0:
        numbers.append(random.randint(0, 10))
    else:
        numbers.append(round(random.uniform(0, 10), 2))
print(numbers)
my_list = []
for el in numbers:
    my_list.append(round(el % 1, 2))
my_list_2 = []
for item in my_list:
    if int(item) != item:
        my_list_2.append(item)
result = round((max(my_list_2)-min(my_list_2)), 2)
print(f'max значение дробной части равно {max(my_list_2)}')
print(f'min значение дробной части равно {min(my_list_2)}')
print(f'Разница между max и min значением дробной части элементов cоставляет {result}')