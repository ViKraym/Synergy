# Есть родительский класс:
# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.


class Transport:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def auto(self):
        print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег {self.mileage}')


# name = input()
# max_speed = input()
# mileage = input()
# h1 = Transport(name, max_speed, mileage)

h1 = Transport("Renaul Logan", 180, 12)
h1.auto()