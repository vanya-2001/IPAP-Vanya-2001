# бонус: добавлен поиск по кнопке Enter
from tkinter import *
from tkinter import ttk
from urllib.request import urlopen
from urllib.parse import urlencode
import xml.etree.ElementTree as et
# from PIL import ImageDraw, Image

class Map:
    def __init__(self):
        self.root = Tk()
        self.root.title('Поиск места по адресу')
        # !! Подкрасил кнопки
        s = ttk.Style()
        s.configure('srch.TButton', background='green')
        s.configure('clear.TButton', background='red')
        s.configure('neg.TButton', background='blue')
        s.configure('pos.TButton', background='orange')
        # иконку приложения добавим позже
        self.root.call('wm', 'iconphoto', self.root._w,
                       PhotoImage(file='icon_info.png'))
        # сохранение цвета фона окна в переменную bgnd


        self.bgnd = self.root['bg']
        self.root.geometry('800x600')
        self.canvas = Canvas(self.root, height=450, width=690)
        self.canvas.place(x=55, y=50)  # левый верхний угол
        # назначаем элементы:
        # предустановленный адрес (начальный адрес)
        self.what_to_find = 'Санкт-Петербург, наб.реки Фонтанка, 119Б'
        self.delta = '0.001'  # для изменения spn
        # текстовое поле, надпись и кнопки
        self.entry = Entry(width=55, font=('Verdana 11'))
        self.srch = ttk.Button(text="Найти адрес", width=15,
                               command=self.show_map, style='srch.TButton').place(x=585, y=1)
        # !!!
        #self.srch = s.configure('one.TButton',  frame=2, fill='blue')
        self.clear_button = ttk.Button(text="Очистить поле", width=15, padding=1,
                                       command=self.clear, style='clear.TButton').place(x=690, y=1)

        # добавили кнопки масштаба - синенькая и + оранжевая
        self.plus = ttk.Button(text='+',  width=5, command=self.positive_zoom,
                               padding=5, style='pos.TButton').place(x=400, y=505)
        self.minus = ttk.Button(text="-", width=5, command=self.negative_zoom,
                                padding=5, style='neg.TButton').place(x=350, y=505)
        self.header = Label(text="Адрес:", font=('Verdana 11')).place(x=5, y=1)
        # размещаем элементы

        self.entry.place(x=60, y=2)
        self.entry.insert(END, self.what_to_find)


        self.show_map()
        # привязываем клавишу Enter к вызову show_map
        self.root.bind('<Return>', self.showMapEnter)
        # ожидание действий
        self.root.mainloop()

    # очистка поля ввода адреса и отображаемой карты
    def clear(self):
        # рисуем прямоугольник, залитый цветом фона
        self.canvas.create_rectangle(0, 0, 691, 451,
                                     outline=self.bgnd, fill=self.bgnd)
        self.canvas.create_rectangle(0, 0, 691, 451,
                                     outline='grey', width=5)
        self.txt = Label(text="Преуспеть в натягивании Карты Яндекс \n "
                              "на желаемый холст не удалось",
                         font=('Verdana 14')).place(x=190, y=235)
        self.entry.delete(0, END)  # удаление введенного текста

    # вызов по нажатию на клавишу Enter (callback)
    def showMapEnter(self, e):
        if self.srch.focus_get().__class__.__name__ == 'Entry':
            self.show_map()

    # кнопка "+" уменьшает spn
    def positive_zoom(self):
        temp = float(self.delta) / 2
        if temp < 0.00025:
            temp = 0.00025
        self.delta = str(temp)
        self.show_map()

    # кнопка "-" увеличивает spn
    def negative_zoom(self):
        temp = float(self.delta) * 2
        if temp > 32.768:
            temp = 32.768
        self.delta = str(temp)
        self.show_map()

    # показываем карту с предустановленным адресом "Можайская 2"
    def show_map(self):
        self.what_to_find = self.entry.get()  # получаем введенный текст
        # если адрес слишком короткий, вводим предустановленный
        if len(self.what_to_find) < 3:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Санкт-Петербург, наб.реки Фонтанка, 119Б')
            self.what_to_find = self.entry.get()

        # пока пустой перечень параметров запроса
        data = {}
        # API-ключ
        data['apikey'] = '40d1649f-0493-4b70-98ba-98533de7710b'
        # адрес по умолчанию
        data['geocode'] = self.what_to_find

        # основная часть ссылки для обращения к геокодеру
        url = 'http://geocode-maps.yandex.ru/1.x/'

        # преобразуем набор параметров в формат URL
        url_values = urlencode(data)
        # формируем полную ссылку
        full_url = '?'.join([url, url_values])
        # получаем ответ по ссылке
        response = urlopen(full_url)

        # полученный ответ преобразуем в XML-формат
        res = response.read().decode('UTF-8')

        # начинаем расшифровывать XML
        root = et.fromstring(res)
        # "вытаскиваем" координаты
        coords = root.find('.//{http://www.opengis.net/gml}pos').text

        # координаты в консоль уже не выводим
        # вновь пустой перечень параметров запроса
        map_data = {}
        # добавляем в запрос все необходимые параметры:
        # широту и долготу
        map_data['ll'] = coords.replace(' ', ',')
        # протяжённость области поиска
        map_data['spn'] = ','.join([self.delta, self.delta])
        # отображаем карту
        map_data['l'] = 'map'
        # добавим значок на карту
        map_data['pt'] = coords.replace(' ', ',') + ',pm2dgl'

        # основная часть ссылки для обращения к
        # статическому контенту Яндекс-карт
        map_url = 'http://static-maps.yandex.ru/1.x/'

        # преобразуем набор параметров в формат URL
        url_values = urlencode(map_data)
        # формируем полную ссылку
        full_url = '?'.join([map_url, url_values])

        # получаем нужный фрагмент
        response = urlopen(full_url)

        # преобразовываем фрагмент в набор пикселей
        self.pict_array = response.read()

        # превращаем набор пикселей в картинку и отображаем её
        self.img = PhotoImage(data=self.pict_array, format='png')
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        # открываем для рисования и создаём рисовальщик
        self.canvas.create_rectangle(0, 0, 691, 451,  outline='grey', width=7)


app = Map()  # помещаем приложение в капсулу и запускаем
