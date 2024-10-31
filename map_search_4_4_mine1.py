from tkinter import *  # подключили все средства библиотеки tkinter
from tkinter import ttk

class Map:
    def __init__(self):
        self.root = Tk()  # создали "корень" нашего приложения
        self.root.title('Поиск места по адресу')  # заголовок окна
        self.root.geometry('800x600')  # размеры окна

#s = ttk.Style()
#s.theme_use('winnative')
#print(s.theme_names(), s.theme_use('alt'))
#
# добавляем элементы GUI
        # надпись и шрифт для неё
        self.label = ttk.Label(text="Адрес:", font=('Verdana 11')).place(x=5, y=2)
        # текстовое поле для поиска и шрифт для него
        self.entry = ttk.Entry(width=50, font=('Verdana 11')).place(x=70, y=2)
        # кнопка с надписью "Найти"
        self.srch = ttk.Button(text="Найти адрес", width=15).place(x=585, y=2)
        # кнопка с надписью "Очистить"
        self.clear_button = ttk.Button(text="Очистить поле", width=15).place(x=690, y=2)
        # ожидание действий
        self.root.mainloop()


app = Map() # помещаем приложение в капсулу и запускаем