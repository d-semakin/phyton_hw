'''
# 30. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt.
# Фрагмент файла с данными о пользователях (users.txt):
# Иванов Иван Иванович
# Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt):
# скалолазание, охота
# горные лыжи
'''

# file1 = open('ForHW4/users.txt', 'r', encoding='utf8')
# users = file1.read()
# file1.close()
#
#
# file2 = open('ForHW4/hobby.txt', 'r', encoding='utf8')
# hobby = file2.read()
# file2.close()
#
# keys = users.split('\n')
# values = hobby.split('\n')
# result = dict(zip(keys, values))
#
# with open('ForHW4/result_HW4Task30.txt', 'w') as f:
#     for key, value in result.items():
#         f.write(f'{key}: {value}\n')

'''
31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
'''

# num = int(input("Введите число: "))
# i = 2
# lst = []
# cnst = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {cnst}: {lst}")

'''
# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")

'''
# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
'''

# import random
# def write_file(st):
#     with open('ForHW4/for_HW4Task33.txt', 'w') as data:
#         data.write(st)
# def rnd():
#     return random.randint(0, 101)
# def create_mn(k):
#     lst = [rnd() for i in range(k + 1)]
#     return lst
# def create_str(sp):
#     lst = sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst) - i - 1}'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr
#
# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))

# 34. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# 2x² + 4x + 5 = 0 и x² + 5x + 3 = 0 => 3x² + 9x + 8 = 0

# from itertools import *
#
# def get_polynomial(k, ratios):  # вычисляем полином, передаем степень и массив коэффициентов
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c in zip_longest(
#         ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x', ' x')
# file1 = 'ForHW4/poly_1.txt'
# file2 = 'ForHW4/poly_2.txt'
#
#
# def read_pol(file):
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol
#
#
# def convert_pol(pol):
#     pol.replace('= 0', '')
#     pol = pol.split(' + ')
#     pol = [i[0] for i in pol]
#     for i in range(len(pol)):
#         if pol[i] == 'x':
#             pol[i] = '1'
#     pol = pol[::-1]
#     return pol
#
#
# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
#
# pol1_coef = list(map(int, convert_pol(pol1)))
# pol2_coef = list(map(int, convert_pol(pol2)))
#
# sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
# sum_coef = sum_coef[::-1]
# sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
# print('Итоговый результат сложения полиномов:\n', sum_pol)
# with open('ForHW4/result_HW4Task34.txt', 'w') as file_sum:
#     file_sum.writelines(sum_pol)