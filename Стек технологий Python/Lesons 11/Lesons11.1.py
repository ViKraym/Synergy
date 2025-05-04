# Урок 11
# Задача 1

def fac(num):

    fakt = 1
    list_num = []

    for i in range(1, num+1):   
            fakt *= i
            list_num.append(fakt)

    return list_num


num = int(input('Натуральное число: '))
list_fakt = fac(num)
list_fakt.reverse()
print(list_fakt)




# Функции

# Дается число на входе, определить четное оно или нет

# Вводится год, на основани года, нужно определить высокосный он или нет (высокосный кратен 4 или 400 не кратен 100)

# def visgod(year):
#     if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#         return True
#     return False
# y = int(input())
# print(visgod(y))

# def nechet(n):
#     return (n % 2 != 0)

# def res(l):
#     for el in l:
#         if nechet(el):
#             print(el)

# tmp = [1, 3, 4, 9, 2, 7]
# res(tmp)

# def new_year():
#     print("Happy new Year!")

# def birthday(name):
#     print(f'Heppy birthday, {name}!')

# def mart8():
#     print('Happy 8th of March')

# n = int(input())
# for i in range(n):
#     cm = input()
#     if cm == 'новый год':
#         new_year()
#     elif cm == 'день рождения':
#         name = input()
#         birthday()
#     elif cm == '8 марта':
#         mart8()
#     else:
#         print('не правильная команда')

