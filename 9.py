# Принципы ООП

# Принцип наследования

# Создание родительского класса (Предковых)

from xml.dom.minidom import Attr


class Animal(object):
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def move(self):
        print('I Moving !')

    def info(self):
        print(f'I have {self.num_legs} legs')

# Создание дочернего класса
class Mammal(Animal):
    def __init__(self, num_legs, name):
        super().__init__(num_legs)
        self.name = name

    def speech(self):
        print(f'my names {self.name}. I have {self.num_legs} legs')
        self.info()

nam_1 = Mammal(2, 'Vasya')
cat_1 = Mammal(4, 'Boris')

# nam_1.move()
# nam_1.info()
# nam_1.speech()

# cat_1.move()
# cat_1.info()
# cat_1.speech()

class Insect(Animal):
    pass
        
bug_1 = Insect(8)

# bug_1.info()
# bug_1.move()

# ****Принчип Полиформизма****

# Полиморфизм операторов
res = 100 + 10 # Сложение
res = '100' + '10' # Конкатенация строк

# Полиморфизм функций
res = len([10,20,30,40,50])
res = len('Python')

# Полиморфизм методов
class A:
    attr_1 = 100
    def m_1(self, arg):
        print(arg + 10)

class B:
    def m_1(self, arg):
        print(arg ** 2)

a = A()
b = B()

# a.m_1(5)
# b.m_1(5)

class C(A):
    def m_1(self):
        print('Stop !',self.attr_1)

c = C()
# c.m_1()

# Полиморфизм с магическими методами (метод перегрузки операторов)

class Sum:
    def __call__(self, a, b):
        print(a + b)
    
    def __str__(self) -> str:
        return 'class Sum создает вызываемые обьекты для сумирования двух чисел'

s = Sum()
# Обьект ведет себя как функция
# s(10, 20)

# print(s)

# Принцип инкасуляции

# Инкапсуляция это режим скрытия свойств и\или методов
# чтобы они не были доступны изза экземпляров класса

# Нет инкапсуляции
class Zed:
    attr = 100

    def m_1(self):
        print(self.attr)

obj_1 = Zed()

# print(obj_1.attr)
# obj_1.m_1()

# не строгая инкапсуляция
class Jet:
    _attr = 100

    def _m_1(self):
        print(self._attr)

obj_1 = Jet()

# print(obj_1._attr)
# obj_1._m_1()

# Cтрогая инкапсуляция
class Y:
    __attr = 100

    def __m_1(self):
        print('__m_1',self.__attr)
    def m_2(self):
        print('m_2',self.__attr)
obj_1 = Y()

# print(obj_1._Y__attr)
# obj_1._Y__m_1()
# obj_1.m_2()


# Принцип композиции (Агрегации)

class Beta:
    def m1(self, arg):
        return arg * 2

class Gamma:
    attr = Beta()

    def m2(self, arg):
        res = self.attr.m1(arg)
        print(res + 10)

obj = Gamma()

obj.m2(5)