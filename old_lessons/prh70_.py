# Обработчик изображений

from tkinter import *  # подключаем все элементы Tkinter
from tkinter import filedialog  # файловый диалог
from PIL import Image, ImageTk


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title('Обработка изображений')
        self.root.geometry('800x600')
        self.root.resizable(True, True)  # Фиксируем габариты
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.label = Label(text='Работаем с картинками', background='black',
                           foreground='red',
                           font=('Verdana', 16))
        self.label.pack()  # (side=TOP, anchor=N,  fill=X, expand=True)
        self.canvas = Canvas(bg='white', height=400, width=600)
        self.canvas.pack(anchor=CENTER, pady=15)
        self.btn = Button(text='Явись!')
        self.btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)
        self.btn.bind('<ButtonPress-1>', self.load)
        self.rect_btn = Button(text='Прямоугольник', command=self.make_rect)
        self.rect_btn.pack(side=LEFT, anchor=N, padx=25, fill=X, expand=True)

        self.image = None
        self.empty = Image.new('RGB', (600, 400), (255, 255, 255))  # пустышка
        self.root.mainloop()

    def load(self, event):
        try:
            fullpath = filedialog.askopenfilename(initialdir='./', filetypes=[
                ('JPEG', '*.jpg'), ('PNG', '*.png'), ('SVG', '*.svg')])
            self.empty = Image.open(fullpath)
            mode = self.empty.mode
            if mode == 'P':  # 256-color indexed image
                self.empty = self.empty.convert('RGB')
            w, h, = self.empty.size
            if w > 600:
                ration = w / 600
                self.empty = self.empty.resize((int(w / ration), int(h / ration)))
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        except AttributeError:
            self.image = ImageTk.PhotoImage(self.empty)
            self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        # self.btn['text'] = 'Заменено'
        # self.btn['text'] = 'Появилось'
        # self.label['text'] = 'Здесь будет картинка'
        # self.label['image'] = self.image

    def make_rect(self):
        self.canvas.create_rectangle(1, 1, 599, 399, outline='#004040', width=3, fill='#80cbc4')


app = App()
