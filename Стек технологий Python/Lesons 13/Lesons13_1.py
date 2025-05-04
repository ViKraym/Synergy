#Задача 1
# Построить две матрицы одинаковой размерности 10 на 10, с рандомным заполнением с помощью модуля random 
# После чего сложить эти матрицу в третью

import random


def pl(t):
    for k in t:
        print(*k)

import random
x = int(input('Введите количество строк (высоту) матрицы: ' ))
y = int(input('Введите количество столбцов (ширену) матрицы: ' ))
matrix1 =   [[ random.randint(-100, 100) for i in range(y) ] for j in range(x)]
matrix2 =   [[ random.randint(-100, 100) for i in range(y) ] for j in range(x)]

result_mrtix = [[matrix1[k][j] + matrix2[k][j] for j in range(y)] for k in range(x)]

pl(matrix1)
print('\n')
pl(matrix2)
print('\n')
pl(result_mrtix)

