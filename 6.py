#  Цыклы

# оператор цицла (while)(пока что)

# Бесконечный цикл
# while True:
    # print('Hello')

# Цикл с условием
# count_1 = 0
# while count_1 < 10:
    # print(f'Значение: {count_1}')
    # count_1 += 1 # Инкремент - увеличение какого либо значения

# count_1 = 10
# while count_1 > -5:
    # print(f'Значение: {count_1}')
    # count_1 -= 1 # Дикремент - уменьшает какое либо значение


# Прерывание цикла по дополнительному условию
# val_1 = 0

# while val_1 < 20:
    # print(f'Значение: {val_1}')
    # val_1 += 1
    # if val_1 == 15:
        # break # Оператор (инструкция) прерывания цикла

# Пропуск кода в теле цикла
# val = 0

#while val < 20:
#    print(f'Значение: {val}')
 #   val += 1
 #   if val < 10:
 #       continue # оператор для пропуска кода с низу(след код) и возвращает обратно
  #  print('Выключение цикла')
  #  break

# Оператор for

# 1. Читает значение итирируемого обьекта по порядку
# 2. Считанное значение присваевается в собственную переменную
# 3. Выполняет блок кода своего тела

#for var1 in [1,2,3,4,5,6,7,8]:
#    var1 += 5
#    print(f'Значение: {var1}')

# var2 = (10,20,30,40,50,60)

#for var1 in var2:
   # var1 += 5
   # print(f'Значение: {var1}')

# Безымянное переменное
#for _ in (1,2,3):
#    print('Hello')

#for char in 'python':
    # res = char * 3
   # res = char.upper()
   # print(res)

# Класс range()

#r = range(10, 51, 10)
#print(list(r))

#for num in range(10, 100, 10):
   # print(num)

# Генератор списка
from tracemalloc import stop


my_list = [num for num in range(10)]

my_list = [num for num in range(10) if num > 5]

my_list = [num for num in range(10) if num % 3 == 0]

my_list = [num ** 2 for num in range(10)]

# Генератор словаря

my_dic = {num : num for num in range(10)}

my_dic = {num : num + 2 for num in range(10)}

my_dic = {num : num + 5 for num in range(10) if num < 5}

# print(my_dic)

# калькулятор

while True:
    com = input('Введите команнду: ')
    if com == 'stop':
        break

    a = input('Введите первое число: ')
    if isinstance(a, int):
        print('Целое цисло')
    elif isinstance(a, float):
        print('Вещественное число')
