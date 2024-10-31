from tkinter import *  # подключили все средства библиотеки tkinter
from tkinter import ttk




class Map:
    def __init__(self):
        self.root = Tk()  # создали "корень" нашего приложения
        self.root.title('Поиск места по адресу')  # заголовок окна
        self.root.geometry('800x600')  # размеры окна

        s = ttk.Style()
        s.configure('one.TButton', background='blue')
        s.configure('second.TButton', background='red')

        #print(s.theme_names(), s.theme_use('vista'))

        #
        # добавляем элементы GUI
        # надпись и шрифт для неё
        self.label = Label(text="Адрес:", font=('Verdana 11')).place(x=5, y=2)
        # текстовое поле для поиска и шрифт для него
        self.entry = Entry(width=50,  font=('Verdana 11')).place(x=70, y=2)
        # кнопка с надписью "Найти"
        self.srch = ttk.Button(text="Найти адрес", width=15, style='one.TButton').place(x=585, y=2)
        # кнопка с надписью "Очистить"
        self.clear_button = ttk.Button(text="Очистить поле", width=15,
                                       style='second.TButton', command=self.clear).place(x=690, y=2)
        # ожидание действий
        self.root.mainloop()


    def clear(self):
        # рисуем прямоугольник, залитый цветом фона
        # self.canvas.create_rectangle(0, 0, 601, 451, outline=self.bgnd, fill=self.bgnd)
        self.entry.delete(0, END)  # удаление введенного текста


app = Map()  # помещаем приложение в капсулу и запускаем
