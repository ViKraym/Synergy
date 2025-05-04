import collections

# pits = dict()

pits = {
        1:
            {
                "Мухтар": {
                    "Вид": "Собака",
                    "Возраст": 9,
                    "хозяин": "Павел"
                },
            },
        2:
            {
                "Каа": {
                    "Вид": "желторотый питон",
                    "Возраст": 19,
                    "хозяин": "Саша"
                },
            },
        }

#============================================Воспамагательные=====================================================================
def get_suffix(age):
    remainder = age % 10
    if age == 0 or remainder == 0 or remainder >= 5 or age in range(11,9):
        suffix = 'лет'
    elif remainder == 1:
        suffix = 'год'
    else:
        suffix = 'года'
    return suffix

def get_pet(pet_id):
    if pet_id in pits.keys():
        return pits[pet_id]
    else:
        return False
#=============================================Воспамагательные====================================================================


def create():
              
        if len(pits) == 0:
            last = 0
        else:
            last = collections.deque(pits, maxlen=1)[0]
        
        last += 1
        print("Укажите имя питомца:")
        name = input()
        card = name
        pits[last] = dict()
        pits[last][card] = dict()
       
        print("Вид питомца:")
        tip_pit = input()
        pits[last][card]["Вид"] = tip_pit
        
        print("Возраст вашего питомца:")
        age_pit = int(input())
        pits[last][card]["Возраст"] = age_pit
        
        print("Имя владельца питомца:")
        owner_pit = input()
        pits[last][card]["хозяин"] = owner_pit
       
        print("\n"f"Карточка питомца успешно добавлен в Базу данных под ID {last}" )

def read(pet_id):
    pet = get_pet(pet_id)
    if pet:
        for pet_name in pet:
            suffix = get_suffix(pet[pet_name]['Возраст'])
            print("\n""Это", pet[pet_name]['Вид'] , "по кличке", pet_name, "Возраст питомца: ", pet[pet_name]['Возраст'], suffix, "Владельца зовут: ", pet[pet_name]['хозяин'])
    else: 
        print("\n""Карточки такого питомца нет в Базе данных")

def update(pet_id):
    pet = get_pet(pet_id)
    pet_name = input('Введите новое имя: ')
    if pet_name == '':
        for name in pet:
            pet_name = name

    pet_tip = input('Введите новое вид: ')
    if pet_tip == '':
       pet_tip = pet[pet_name]["Вид"] 

    pet_age = input('Введите новое возраст: ')
    if pet_age == '':
       pet_age = pet[pet_name]["Возраст"] 

    pet_owner = input('Введите нового хозяина: ')
    if pet_owner == '':
       pet_owner = pet[pet_name]["хозяин"] 

    pits[pet_id] = {
                pet_name: {
                    "Вид": pet_tip,
                    "Возраст": int(pet_age),
                    "хозяин": pet_owner
                }
            }
    print(pits)
   
    
def delete(pet_id):
    val = get_pet(pet_id)
    if val:
        pits.pop(pet_id)
        print(f'Карточка питомца с ID {pet_id} успешно удалена из БД')
    return print("\n""Карточки такого питомца нет в Базе данных")

def pets_list():
    pass 



#=================================================================================================================================#


card = dict()

print("Добро пожаловать в клинику.")
command = 0 

while command != 'stop':
    print('\n'"Выберете действие для продолжения""\n")
    print("1 - Создать новую запись о питомце")
    print("2 - Посмотреть карточку питомца")
    print("3 - Изменить существующую запись/внести корректировки")
    print("4 - Удалить запись о питомце")
    print("Чтобы закончить работу с Базой данных - Введите stop"'\n')

    command = input()
    command.lower()
      
    if command == "1":
        create()

    elif command == "2":
        print("Введите ID питомца")
        pet_id = int(input())
        read(pet_id)

    elif command == "3":
        print("Введите ID питомца")
        pet_id = int(input())
        update(pet_id)  

    elif command == "4":
        print("Введите ID питомца")
        pet_id = int(input())
        delete(pet_id)
  