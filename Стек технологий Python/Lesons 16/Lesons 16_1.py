# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:

# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Kassa(object):
    def __init__(self, count = 0):
        self.count = count

    def top_up(self, add):
        self.count += add
        print("В кассе теперь: ", self.count)
            
    def count_1000(self):
        self.count = self.count // 1000
        print("В кассе лежит: ", self.count, "купюр номиналом в 1000")

    def take_away(self, pop):
        if self.count > pop:
            self.count -= pop
            print("В кассе осталось: ", self.count)
        else:
            print("В кассе недостаточно наличных")       

K1 = Kassa()

while True:
    
    print("Какую операцию нужно произвести?")
    print("1. Положить в кассу")
    print("2. Посчитать купюры номиналом 1000")
    print("3. Забрать из кассы")
    print("4. Закрыть кассу")
    a = int(input())
    
    if a == 1:
        add = int(input('Положить в кассу: '))
        K1.top_up(add)
    elif a == 2:
        K1.count_1000()

    elif a == 3:
        pop = int(input('Забрать из кассы: '))
        K1.take_away(pop)
        
    elif a == 4:
        exit()
    else:
        print("Вы ввели несоответствующее значение")
    

 