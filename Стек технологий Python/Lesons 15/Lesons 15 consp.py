class Human(object):
    name = "Ivan"
    height = 175
    age = 25

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def privet(self):
        print(f'My name is {self.name}, my age is {self.age}')

    def get_older(self):
        self.age += 5

    def goodbay(self):
        print("goodbay")

h1 = Human('Anton', 120, 12)
h2 = Human('Petr', 190, 23)

h1.goodbay()