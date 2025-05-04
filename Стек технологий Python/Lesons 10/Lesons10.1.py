# Bank = dict()
# n= int(input())

# for i in range(n):
#     req = input()
#     if req == "create":
#         k = input()
#         Bank[k] = 0
#     elif req == "add":
#         k = input()
#         amount = int(input())
#         if k in bank.keys():
#             Bank[k] += amount
#         else:
#             print("sorry, no such key")
#     else:
#             print("sorry, bad request")
# print(Bank)

# tmp = {"k1": 1, "k2": 10, "qwert": 5}
# bank = dict()
# print(tmp.keys())
# print(tmp.values())
# print(tmp.items())
# tmp.pop('k1')

# for k in tmp.keys():
#     print(k)


# company = {
#     "pits": {
#         "Alice": {"age": 25, "role": "Sales Executive"},
#         "Bob": {"age": 30, "role": "Sales Manager"}
#     },
   
# }

company = dict()
    
while True:
    print()
    print("Добро пожаловать в клинику. Какой у вас вопрос?""\n")
    print("1 - Записать питомца")
    print("2 - Посмотреть анкету питомца")
    print("0 - Забрать питомца")

    req = input()
    if req == "1":
        print("Как зовут вашего питомца?")
        name = input()
        company[name] = dict()

        print("Вид вашего питомца:")
        tip_pit = input()
        company[name]["вид"] = tip_pit

        print("Возраст вашего питомца:")
        age_pit = int(input())
        if (age_pit % 10 == 1) and (age_pit != 11) and (age_pit % 100 != 11):
            year_case = str(age_pit) + ' год'

        elif (1 < age_pit % 10 <= 4) and (age_pit != 12) and (age_pit != 13) and (age_pit != 14):
            year_case = str(age_pit) + ' года'  
            
        else:
            year_case = str(age_pit) + ' лет'
        
        company[name]["Возраст"] = year_case

        print("Имя владельца питомца:")
        owner_pit = input()
        company[name]["хозяин"] = owner_pit
        
        print("\n""Ваш питомец успешно добавлен в список нашей клиники")
    
    elif req == "2":
        print("Как зовут вашего питомца?")
        name = input()
        if name in company:
            print("\n""Это", company[name]['вид'], "по кличке", name, "Возраст питомца: ", company[name]['Возраст'], "Владельца зовут: ", company[name]['хозяин'])
        else:
            print("\n""Простите, но такого питомца нам не оставляли")

    elif req == "0":
        print("Как зовут вашего питомца?")
        name = input()
        if name in company:
            print("\n""Вот ваш питомец")
            company.pop(name)
        else:
            print("\n""Простите, но такого питомца нет")

        


