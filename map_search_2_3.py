from tkinter import * # подключили все средства библиотеки tkinter
 
# определяем функцию clear
# т.е. набор команд для очистки поля ввода адреса
# вот и первый отступ в четыре пробела
# он ставится на следующей строке после двоеточия
# и означает принадлежность команд функции clear
 
def clear():
    # удаление всего введенного текста
    # (от нулевого и до последнего символа)
    entry.delete(0, END)
    # получаем цвет фона окна окна
    bgnd = root['bg']
    # заполняем этим цветом холст (эффект удаления)
    canvas = Canvas(bg=bgnd, width=600, height=450)
    canvas.place(x=100, y=50)
    
 
def show_map():
    # получаем текст из поля ввода
    bgnd = entry.get()
    # пробуем применить данный текст в качестве цвета
    try:
        canvas = Canvas(bg=bgnd, width=600, height=450)
    # в случае неудачи красим в серый цвет
    except:
        canvas = Canvas(bg='gray', width=600, height=450)
    canvas.place(x=100, y=50) # левый верхний угол
 
 
root = Tk() # создали "корень" нашего приложения
root.title('Поиск места по адресу') # заголовок окна
root.geometry('800x600') # размеры окна
 
 
# добавляем элементы GUI
# надпись и шрифт для неё
header = Label(text="Адрес:", font=('Verdana 12'))
# текстовое поле для поиска и шрифт для него
entry = Entry(width=60, font=('Verdana 12'))
# кнопка с надписью "Найти"
srch = Button(text="Найти", command=show_map)
# кнопка с надписью "Очистить"
clear_button = Button(text="Очистить", command=clear)
 
# размещаем элементы с помощью place
header.place(x=5, y=0) # надпись
entry.place(x=70, y=2) # текстовое поле
srch.place(x=685, y=0) # кнопка "Найти"
clear_button.place(x=735, y=0) # кнопка "Очистить"
 
# ожидание действий
root.mainloop()
