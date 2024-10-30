# GUI - Graphic User Interface
# PyQt6 - на самостоятельное
import tkinter

from PIL import Image, ImageTk

# корневой элемент приложения
root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.grid()
# Добавляем ярлык
label = tkinter.Label(frame, text='GUI').grid_configure(row=1, column=1)
# Добавляем кнопку
but = tkinter.Button(frame, text='Кнопка').grid_configure(row=2, column=1)

# Добавим холст
canvas = tkinter.Canvas(root, width=600, height=400)

# Добавляем изображение на холст
image = Image.open('original.jpg')
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid_configure(row=2, column=2)
root.mainloop()
