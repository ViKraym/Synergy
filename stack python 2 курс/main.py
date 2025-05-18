# def my_print():
#     print('Hello world')

# my_print()

# def my_sum(a,b):
#     return a + b

# print(my_sum(2, 7))

# def my_sum2(a,b=5):
#     return a + b

# print(my_sum2(2))

# def my_print2(print_string="hello world"):
#     print(print_string)

# my_print2()
# my_print2('asdasdasd')

# def hello_str(): return 'hello'
# def bye_str(): return 'bye'

# def my_print_from_func(func):
#     print(func())
    
# print(hello_str)

# # my_print_from_func('asfdasf')

# def my_print_from_func_2(func):
#     if callable(func): print(func())
#     else: print('func is not callable')
    
# my_print_from_func_2('asfdasf')

#----------------------klass-----------------------------------------------------------------


# class Employee:
#     def __init__(self, age, name, salary) -> None:
#         self.age = age
#         self.name = name
#         self.salary = salary
        
#     def get_salary(self):
#         return self.salary
    
# class Programmer(Employee):
#     def __init__(self, age, name, salary) -> None:
#         super().__init__(age, name, salary)
        
# class Manager(Employee):
#     def __init__(self, age, name, salary):
#         super().__init__(age, name, salary)
        
#     def get_salary(self):
#         return super().get_salary() * 1.3
    
    
# if __name__ == '__main__':
    
#     programmer = Programmer(30, 'Владимир', 100000)
#     print(programmer.name, programmer.salary, programmer.get_salary())
    
#     manager = Manager(20, 'Александр', 120000)
#     print(manager.name, manager.salary, manager.get_salary())


#----------------------абстрактные klass-----------------------------------------------------------------

# from abc import abstractmethod

# class Employee:
#     def __init__(self, age, name, salary) -> None:
#         self.age = age
#         self.name = name
#         self.salary = salary
        
#     @abstractmethod   
#     def get_salary(self):
#         raise NotImplementedError('Method not Implemented')
        
# class Programmer(Employee):
#     def __init__(self, age, name, salary) -> None:
#         super().__init__(age, name, salary)
    
#     def get_salary(self):
#         return self.salary
        
# class Manager(Employee):
#     def __init__(self, age, name, salary):
#         super().__init__(age, name, salary)
        
#     def get_salary(self):
#         return super().get_salary() * 1.3
    
    
# if __name__ == '__main__':
    
#     programmer = Programmer(30, 'Владимир', 100000)
#     print(programmer.name, programmer.salary, programmer.get_salary())
    
    # manager = Manager(20, 'Александр', 120000)
    # print(manager.name, manager.salary, manager.get_salary())
    


#----------------------SOLID-----------------------------------------------------------------

#----------------------    S       -----------------------------------------------------------------

#---Принцип первой обязанности требует того, чтобы ОДИН класс выполнял только ОДНУ работу. 
#---таким образом, если у класса есть БОЛЕЕ одной работы(задачи), он становится зависимым. Из чего следует что, 
#---если изменить принцип работы одной задачи, приведет к изменению второй

'''НЕ ПРАВИЛЬНО'''
class User:
    def __init__(self, name: str):
        self.name = name
        
    def get_name(self) -> str:
        pass
    
    def save(self, user):
        pass
    
'''ПРАВИЛЬНО'''

class User:
    def __init__(self, name: str):
        self.name = name
        
    def get_name(self) -> str:
        return self.name
    
    
class UserDB:

    def get_user(self, id) -> User:
        
        """
        
        Запрос в базу данных
        
        """
        pass

    def save(self, user: User):
         """
        
        Запрос в базу данных
        
        """
        pass

#----------------------        О       -----------------------------------------------------------------

#---Программные сущности (классыб модулиб функции) должны быть открыты для РАСШИРЕНИЯ, но НЕ МОДИФИКАЦИИ. 

# НЕ ПРАВИЛЬНО

# class Discount:
#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price
        
#     def give_discount(self):
#         if self.customer == 'fav':
#             return self.price * 0.2
#         if self.customer == 'vip':
#             return self.price * 0.4


# ПРАВИЛЬНО

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
        
    def get_discount(self):
        return self.price * 0.2
    
class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2
    

class SuperVIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 4
        
#----------------------        L       -----------------------------------------------------------------

#---Принцип подстановки ЛИСКОВ. Идея заключается в том, что для любого класса клиент должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними, и следовательно
#---без каких либо изменений поведения программы. Это означает, что клиент полностью изолирован и не подозревает об изменениях в иерархии классов 

# НЕ ПРАВИЛЬНО

class Employee:
    def __init__(self, data) -> None:
        self.age = data[0]
        self.name = data[1]
        self.salary = data[2]
        
    def set_salary(self, salary):
        self.salary = salary
    

class Accountant(Employee):
    
    def __init__(self, data) -> None:
        super().__init__(data)
        
    def set_coef(self, coef):
        self.coef = coef
        
# ПРАВИЛЬНО

class Employee:
    def __init__(self, age, name, salary) -> None: #значение в скобках (передаваемые значения)
        self.age = age
        self.name = name
        self.salary = salary
        
    def set_salary(self, salary):
        self.salary = salary
        
    def set_salary(self, coef = 0.1):
        self.coef = coef
        
class Accountant:
    
    def __init__(self, age, name, salary) -> None:
        super().__init__(age, name, salary)
        
    def set_coef(self, coef = 0.5):
        self.coef = coef
        
#----------------------        I       -----------------------------------------------------------------

#---Принцип разделения интерфейсов.
#---Создавайте тонкие интерфейсы, которые ориентированы на клиента. Клиенты не должны зависить от интерфейсов,
#---которые они не используют. Этот принцип устраняет недостатки реализации больших интерфейсов

# НЕ ПРАВИЛЬНО 

class Creature:
    def __init__(self, age):
        self.age = age
    
    def run(self):
        pass
    
    def swim(self):
        pass
    
    def speak(self):
        pass
    
class Human(Creature):
    ...
    
class Cat(Creature):
    ...
    
#ПРАВИЛЬНО 

class Creature:
    def __init__(self, age):
        self.age = age
        

class RunInterface:
    def run(self):
        pass

class SwimInterface:
    def swim(self):
        pass

class SpeakInterface:
    def speak(self):
        pass
    
class Human(Creature, RunInterface, SwimInterface, SpeakInterface):
    ...
    

class Cat(Creature, RunInterface, SwimInterface):
    ...
    

if __name__ == '__main__':
    cat = Cat(5)
    cat.speak()
    
#----------------------        D       -----------------------------------------------------------------

#---Принцип инверсии зависимостей.
#---Зависимость должна быть от абстраций, а не от конкретики.
#---Модули верхних уровней не должны зависеть от модулей нижних уровней.
#---Классы и верхних и нижних уровней должны зависеть от одних и тех же абстракций.
#---Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций

# НЕ ПРАВИЛЬНО 

class ElkLogging:
    def log(str):
        print(str)
    
class ConsoleLogging:
    def log(str):
        print(str)

class logger():
    def __init__(self):
        self.elk_logging = ElkLogging()
        self.console_logging = ConsoleLogging()
        
    def elk_log(self, log):
        self.elk_logging.log(log)
    
    def console_log(self, log):
        self.console_logging.log(log)
        
    
#ПРАВИЛЬНО 

class ElkLogging:
    def log(str):
        print(str)
        
class ConsoleLogging:
    def log(str):
        print(str)

class logger():
    def __init__(self, logging_wrapper):
        self.logging_wrapper = logging_wrapper
    
     def log(self, log):
        self.logging_wrapper().log(log)