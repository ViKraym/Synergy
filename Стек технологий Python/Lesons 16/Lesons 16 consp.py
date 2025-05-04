# class Car(object):
#     brand = 'Mazda'
#     max_speed = 100
#     color = 'Black'

#     def __init__(self, b, ms):
#         self.brand = b
#         self.max_speed = ms

#     def upgrade(self):
#         self.max_speed += 25


# class Truck(Car):
#     max_weight = 10


#     def __init__(self, b, ms, mw):
#         super().__init__(b, ms)        
#         # self.brand = b
#         # self.max_speed = ms
#         self.max_weight = mw

#     def add(self):
#         self.max_weight += 10
    

# gazel = Truck('Gazel', 60, 120)
# print(gazel.brand, gazel.color, gazel.max_weight, gazel.max_speed)



# nissan = Car('Nissan', 190)
# print(nissan.brand, nissan.max_speed)

# mazda = Car('Mazda', 190)
# mazda.upgrade()
# print(mazda.max_speed)


# gazel = Truck('Gazel', 60)
# gazel.upgrade()
# gazel.add()
# print(gazel.brand)
# print(gazel.max_speed)
# print(gazel.max_weight)
# =====================================================================================================================
# Приватность полей (свойств и методов классов)

# Приватное свойство

# class Car(object):
#     brand = 'Mazda'
#     max_speed = 100
#     color = 'Black'
#     # disk_size = 25
#     __password = 1234

#     def __init__(self, b, ms):
#         self.brand = b
#         self.max_speed = ms

#     def upgrade(self):
#         self.__password = 9524 #так делать получится
#         self.max_speed += 25

#     def get_password(self):
#         return self.__password


# tmp = Car('Mazda', 190)
# print(tmp.get_password())

# tmp = Car('Lada', 2)
# tmp.disk_size = 45

# print(tmp.disk_size)
# 
# # Приватный метод

class Car(object):
    brand = 'Mazda'
    max_speed = 100
    color = 'Black'
    __password = 1234

    def __init__(self, b, ms):
        self.brand = b
        self.max_speed = ms

    def __update_password(self):
        self.__password = 9524

    def upgrade(self):
        self.max_speed += a
        self.__update_password()

    def get_password(self):
        return self.__password
    
a = int(input())
tmp = Car('Mazda', a)
print(tmp.max_speed)
tmp.upgrade()
print(tmp.max_speed)