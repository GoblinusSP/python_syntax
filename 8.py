# ООП обьектна ориентированная програмирование

# все является обьектом
# Обьекты обладают свойствами и методами(способностями)
# Обьекты относятся к определенным классам (типам данных)
# Класс - 'Чертеж' обьекта.
# Обьекты = экземпрял (инстанс) класса.

# Создание (определение) класса


class Cat:
    # Свойства(атрибуты)
    name = None
    age = None

# Создание эксемпляр (обьекта) класса Cat
cat_1 = Cat()
cat_2 = Cat()
cat_3 = Cat()

# print(cat_1, cat_2, cat_3)

# Считывание значения у свойтсв
# print(cat_1.name, cat_2.name, cat_3.name)

# Запись значение в свойсвто
cat_1.name = 'Vasya'
cat_2.name = 'Boris'
cat_3.name = 'Bars'

# print(cat_1.name, cat_2.name, cat_3.name)

class Cat_2:
    # метод-конструктор(относится к "магическим" методом(метод перегрузки операторов))
     def __init__(self, name, agr_age):
         # Свойства
         self.name = name
         self.age = agr_age

# Обьявление эксземпляра класса с передачей параметров для свойств
cat_1 = Cat_2('Taba', 5)
cat_2 = Cat_2('Var', 4)
cat_3 = Cat_2('Sab', 6)

# print(cat_1.name, cat_2.name, cat_3.name)
# print(cat_1.age, cat_2.age, cat_3.age)

class Cat_3:
    # Метод конструктор
    def __init__(self, name: str, age: int) -> None:
       self.name = name
       self.age = age
       weight = 100

    # Метод (атрибут-метод) - функция, принадлежащая к классу
    def mur(self):
        print('Mau, Mau') 

    def speech(self):
        tekst = f'Здарова !! я {self.name}, я не ел {self.age} лет !!'
        print(tekst)

    def cumpute(self, a, b):
        return a + b


cat_1 = Cat_3('Vasya', 33)
cat_2 = Cat_3('Baha', 22)
cat_3 = Cat_3('PEN', 11)

# Вызов методов
cat_1.mur()
cat_2.mur()
cat_3.mur()

cat_1.speech()
cat_2.speech()
cat_3.speech()

print(cat_1.cumpute(2, 5),
cat_2.cumpute(3, 1),
cat_3.cumpute(6, 10))