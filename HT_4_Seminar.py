"""
1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

from random import randint

def random_list(length):
    array = []
    for i in range(length):
        array.append(randint(0, 10))
    print(array)
    return array

def sum_of_uneven(input_list):
    sum = 0
    for i in range(1, len(input_list), 2):
        sum=sum+input_list[i]
    return sum

rnd=random_list(10)
print(sum_of_uneven(rnd))

"""
2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
"""

def mean_of_vec(input_vector):
    sum=0
    for i in range(len(input_vector)):
        sum=sum+input_vector[i]
    return sum/len(input_vector)

def rnd_two_d_array_wth_mean_of_rows (rows, cols):
    row_vec=[]
    two_d_array=[]
    for i in range(rows):
        for j in range(cols):
            row_vec.append(randint(0, 10))
        two_d_array.append(row_vec)
        print(f'Среднее арифметическое {i+1}-й строки равно: {mean_of_vec(row_vec)}')
        row_vec=[]
    print(two_d_array)

rnd_two_d_array_wth_mean_of_rows(2, 4)

"""
3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
"""

def list_of_rnd_thirty():
    array = []
    for i in range(30):
        array.append(randint(0, 10))
    print(array)
    return array


def selection_sort(input_array):
    for i in range(len(input_array)):
        min_value = min(input_array[i:])
        min_index = input_array[i:].index(min_value)
        input_array[i], input_array[i+min_index] = input_array[i+min_index], input_array[i]
    print(input_array)


rnd_array = list_of_rnd_thirty()
selection_sort(rnd_array)
