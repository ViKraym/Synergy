def last_position(x, a = 0):
    if a < len(x):
        print(x[a])
        last_position(x, a + 1)                       
    else:
        return print("Конец списка")
        

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

last_position(my_list)