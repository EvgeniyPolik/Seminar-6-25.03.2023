"""
Задача 2: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

n = int(input('Введите количество элементов: '))
exp_list = [random.randint(-100, 100) for i in range(n)]
print('Наш массив: ', *exp_list)
min_value = int(input('Введите минимальный элемент: '))
max_value = int(input('Введите максимальный  элемент: '))
print(*[z for z in range(len(exp_list)) if min_value <= exp_list[z] <= max_value])
