# Коллекция 

# Список (list)

# Создание пустого списка 
list_1 = []
list_2 = list()

# Создание заполненного списка
list_3 = [10, 20, 7, 3.14, 'python', '!',[1,2,3]]

# Добавление элемента в список
list_1.append(1000)
list_1.append('A')

list_3.append(0.0)

# Добавление элемента в список по индексу
list_3.insert(3, 'Hi')

# Добавление итерируемых элементов в список
list_3.extend([100, 200])
list_3.extend('Hello')

# Чтение значений элементов списка
# Прямая индексация
el_1 = list_3[0]
#el_2 = list_3[5]
# Узнаем колличество элементов (длину) списка
# print(f"Длинна списка равна = {len(list_3)}")

el_2 = list_3[15]

# Обратная индексация
el_3 = list_3[-2]

# print(list_3)
# print(el_3)

# Чтение значений вложенных коллекций
list_4 = [[1,2,3],[10,20,30,40,50]]

# print(list_4[1][2])

# Замена значений 
list_5 = list('Hello, world!')

list_5[1] = 100

# Удаление элемента по индексу
del list_5[-1]

# Удаление по значению (первое совпадение)
list_5.remove('l')

# print(list_5)

# Срезы списка
list_5 = list('Hello, world!')
# Срез от начало и до какого то индекса, конечный индекс не включается в срез
slice_1 = list_5[0:5]
slice_1 = list_5[:5]

# Срез от произвольного индекса А до индекса Б
slice_2 = list_5[2:5]

# Срез от произвольного индекса А до конца списка
slice_3 = list_5[6:]

# Срез от произвольного индекса А до индекса Б c шагом С
slice_4 = list_5[1:10:2]

# Срез от произвольного индекса А до индекса Б c шагом С в обратном направлении
slice_5 = list_5[-2:-10:-2]

# Перевернули список 
slice_6 = list_5[::-1]



print(list_5)
print(slice_6)