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
        # имя файла картинки (пока пустое)
        self.filename = ''
        # сохранение цвета фона окна в переменную bgnd
        self.bgnd = self.root['bg']
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
        # создаём синий холст и размещаем его в окне
        self.canvas = Canvas(self.root, bg='blue', width=600, height=450)
        self.canvas.place(x=100, y=50) # левый верхний угол
        # после того, как все необходимые данные были созданы
        self.root.mainloop() # ожидаем действий пользователя
 
    def clear(self):
        # рисуем прямоугольник, залитый цветом фона
        self.canvas.create_rectangle(0, 0, 601, 451,
                                     outline=self.bgnd, fill=self.bgnd)
        # удаление всего введенного текста:
        # от нулевого и до последнего символа
        self.entry.delete(0, END)
 
    def show_map(self):
        # читаем содержимое текстового поля
        self.filename = self.entry.get()
        try:
            # пробуем открыть файл изображения из self.filename
            self.img = PhotoImage(file=self.filename)
            # и разместить его на холсте
            self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        except:
            # при неудаче: рисуем залитый серым прямоугольник
            self.canvas.create_rectangle(0, 0, 601, 451,
                                     outline='gray', fill='gray')
 
 
# создаём объект (размещаем всё в памяти)
app = App()
