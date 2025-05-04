def get_suffix(age):
    remainder = age % 10
    if age == 0 or remainder == 0 or remainder >= 5 or age in range(11,9):
        suffix = 'лет'
    elif remainder == 1:
        suffix = 'год'
    else:
        suffix = 'года'
    return suffix

print(35009%10)

# назовите ID питомца карточку котрого вы хотите отредактировать
# ввод пользователя
# какую информацию вы хотите изменить? 
#     1 вид
#     2 имя
#     3 возраст
#     4 имя владельца
# пользователь хочет изменить возраст (тоесть 3)
# Введите новые данные
# ввод пользователя
# уточняющий вопрос, хотители вы изменить что-то еще?
# да или нет

пустой список
перебор for val in pet.values():
    добавить val в список

 # for k, val in pet.items():
    #     print('\n'f"Введите {k}")
    #     a = input()
    #     if a != '':
    #         pits[pet_id] = {a:val}
    #     for j in val.keys():
    #         print('\n'f"Введите {j}")
    #         b = input()
    #         if b != '':
    #             pits[pet_id][k][j] = b