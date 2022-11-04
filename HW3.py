'''
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
*Пример: *

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
def SumOfOddElements (arr):
    summ = 0
    for i in range(1, len(arr), 2):
        summ += arr[i]
    print(f'Cумма элементов списка {arr } на нечётных позициях: {summ}')

arr = [2, 3, 5, 9, 3]
SumOfOddElements(arr)

'''
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и 
предпоследний и т.д.
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
def MultPairsNumbers (arr):
    newarr =[]
    for i in range((len(arr)+1)//2):
        newarr.append(arr[i]*arr[len(arr)-1-i])
    print(f' Исходный список: {arr}, сформированный по условиям задачи: {newarr}')

arr1 = [2, 3, 4, 5, 6]
arr2 = [2, 3, 5, 6]

MultPairsNumbers(arr1)
MultPairsNumbers(arr2)

'''
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
def DiffMaxMin (arr):
    newarr = [round(i % 1, 2) for i in arr if i % 1 != 0]
    print(max(newarr) - min(newarr))

arr = [1.1, 1.2, 3.1, 5, 10.01]

DiffMaxMin(arr)

'''
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

def DecimalToBinary ():
    s = ""
    n = int(input("Введите число для преобразовывания десятичного числа в двоичное: "))
    while n != 0:
        s = str(n%2) + s
        n //=2
    print(s)

DecimalToBinary()

'''

5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''


def FullFibonacci():
    def Fibonacci(n):
        if n in [1, 2]:
            return 1
        else:
            return Fibonacci(n - 1) + Fibonacci(n - 2)

    def NegaFibonacci(n):
        if n == 1:
            return 1
        elif n == 2:
            return -1
        else:
            num1, num2 = 1, -1
            for i in range(2, n):
                num1, num2 = num2, num1 - num2
            return num2

    arr = []
    n = int(input('Введите число: '))
    for e in range(1, n + 1):
        arr.append(Fibonacci(e))
        arr.insert(0, NegaFibonacci(e))
    print(arr)


FullFibonacci()
