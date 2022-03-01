# Программа с графическим поьзовательским интерфейсом (GUI)

# Генератор паролей 

import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar

def generator():
    # чтение строки сырого пароля
    pwd_str = pwd.get()

    # кодирование в байт строку
    byte_str = pwd_str.encode()

    # хеширование
    hash_str = hashlib.sha256(byte_str)
    
    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]

    # Вывод хеш строки
    # print(hex_str)
    hash_pwd.set(hex_str)

# Создание окна
window = Tk()
window.title('Генератор паролей v.0.1')

# обьекты для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# Виджет (компонент) текстовой метки
lbl = Label(text='Пароль : ')
lbl.grid(row=0, column=0)

# виджет поля ввода сырой пароли
Entry(textvariable=pwd).grid(row=0, column=1)

# виджет кнопки
Button(text='Погнали!', command=generator).grid(row=1, column=0)

# виджет поля вывода зашированной пароли
Entry(textvariable=hash_pwd).grid(row=1, column=1)


# Точка входа программы (место, где программа запускается)
window.mainloop()