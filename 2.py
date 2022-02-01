# Функции ввода и вывод
in1 = input('Введите число :')
in2 = input('Введите второе число :')
#print(in1, in2)

#Типы данных
# int 
#int(in1)
# float
#float(in1)
# str
#str(in1)
# bool
#true or false

# Арифметические операции
int(in1, in2)
in3 = int(input('Выберите действие которое надо совершить(1-сложение,2-вычетание,3-умножение,4-деление) :'  ))

if in3 == 1:
    print(in1 + in2)
elif in3 == 2:
    print(in1 - in2)
elif in3 == 3:
    print(in1 * in2)
elif in3 == 4:
    print(in1 / in2)
else:
    print('Ошибка !')
# //-деление целого, %-деление по остатку, **- возведение в степень


# Способ форматировангие строки "f-строка"
#fs_1 = f'Fisrt number:{in1}, Second number: {in2}'

#fs_2 = f"""
#Fisrt number: {in1}
#Second number: {in2}"""
# \t-таабуляция \n-новая строка
#fs_3 = f'\nFisrt number: \t{in1}, \nSecond number: \t{in2}'


#print(fs_1)
#print(fs_2)
#print(fs_3)
