from tkinter import * # подключили все средства библиотеки tkinter
 
root = Tk() # создали "корень" нашего приложения
root.title('Поиск места по адресу') # заголовок окна
root.geometry('800x600') # размеры окна
 
# добавляем элементы GUI
# надпись и шрифт для неё
header = Label(text="Адрес:", font=('Verdana 12'))
# текстовое поле для поиска и шрифт для него
entry = Entry(width=60, font=('Verdana 12'))
# кнопка с надписью "Найти"
srch = Button(text="Найти")
# кнопка с надписью "Очистить"
clear_button = Button(text="Очистить")
 
# размещаем элементы с помощью place
header.place(x=5, y=0) # надпись
entry.place(x=70, y=2) # текстовое поле
srch.place(x=685, y=0) # кнопка "Найти"
clear_button.place(x=735, y=0) # кнопка "Очистить"
 
# ожидание действий
root.mainloop()
