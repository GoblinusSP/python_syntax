# Функции 

# Создание (определение) функции

# 1 вариант. функция которая не принимает данные (нет аргументов) и при этом ничего не возвращает
def func_1 () -> None:
    '''
    Первая функция
    '''
    var_1 = 100
    var_2 = 150
    res = var_1 * var_2
    print(res)

# Вызов функции
# func_1()

# 2 Вариант. функция которая принимающая параметры (обладающая аргументами) и ничего не возвращет
def func_2 (arg_1):
    res = arg_1 ** 2
    print(res)
# func_2 (100)

# Пример
import math

def func_3 (arg1: tuple, arg2: tuple, arg3: str) -> None:
    '''
    Вычесляет ефклидовое растояние между двумя точками

    Параметры(аргументы):
    ---------
    arg1: tuple 
        кординаты первой точки
    arg2: tuple
        кординаты второй точки
    arg3: str
        название
    '''
    katet_x = (arg1[0] - arg2[0]) ** 2
    katet_y = (arg1[1] - arg2[1]) ** 2

    gipotinuza = math.sqrt(katet_x + katet_y)

    print(f'{arg3}: {gipotinuza}')

point1 = (20, 5)
point2 = (0, -10)

# func_3(point1, point2, 'Растояние')

def func_4 (a, b, c):
    print(a + b * c)

# позиционная передача параметров
# func_4(10, 20, 5)

# Именованная передача параметров
# func_4(a=10, b=20, c=2)

def func_5 (a, b=10, c=20):
    print(a + b + c)
# func_5(a = 10)
# func_5(10,c = 30)


# Передача произвольного колличества позиционных параметров
# print(10,20,30,40,50)

def func_6(*args):
    print(args)

    res = args[0] + args[2]
    print(res)

    s = 0
    for n in args:
        s += n
    print(s)

# func_6(10,20,30,40,50,60)

# Передача произвольного колличества именованных параметров

def func_7(**kwargs):
    print(kwargs)

    res = kwargs['a'] + kwargs['c']
    print(res)

    for item in kwargs.items():
        print(f'Ключ: {item[0]},Значение:{item[1]}')

# func_7(a=100, b=200, c=300)

# Функия принимающая параметры и возвращающая значения

def func_8(arg1, arg2):
    res = arg1 + arg2
    return res

var_1 = func_8(10,20)

# print(var_1)

def func_9(arg1, arg2):
    res1 = arg1 + arg2
    res2 = arg1 > arg2
    return res1, res2

# print(func_9(10, 10))