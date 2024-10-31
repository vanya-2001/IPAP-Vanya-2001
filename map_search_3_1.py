from tkinter import * # подключили все средства библиотеки tkinter
 
 
# создадим класс App (от слова Application)
# всё, что классу принадлежит, сдвинуто на
# четыре пробела (после двоеточия)
class App():
    # все создаваемые данные "размещаются"
    # в конструкторе __init__()
    def __init__(self):
        # всё, что принадлежит __init__()
        # также сдвинуто на четыре пробела
        self.root = Tk() # создали "корень" нашего приложения
        self.root.title('Поиск места по адресу') # заголовок окна
        self.root.geometry('800x600') # размеры окна
        # добавляем элементы GUI
        # надпись "Адрес:" и шрифт для неё
        self.header = Label(text="Адрес:", font=('Verdana 12'))
        # текстовое поле для поиска и шрифт для него
        self.entry = Entry(width=60, font=('Verdana 12'))
        # кнопка с надписью "Найти"
        self.srch = Button(text="Найти", command=self.show_map)
        # кнопка с надписью "Очистить"
        self.clear_button = Button(text="Очистить", command=self.clear)
        # размещаем элементы с помощью place
        self.header.place(x=5, y=0) # надпись
        self.entry.place(x=70, y=2) # текстовое поле
        self.srch.place(x=685, y=0) # кнопка "Найти"
        self.clear_button.place(x=735, y=0) # кнопка "Очистить"
 
    def clear(self):
        # пока только объявление
        pass
 
    def show_map(self):
        # пока только объявление
        pass
 
 
# создаём объект (размещаем всё в памяти)
app = App()
 
