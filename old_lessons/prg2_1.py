import turtle as t  # подключение внешней  библиотеки
# prg_1.py snake case PYTHON !ПРАВИЛА ХОРОШЕГО ТОНА!
# forstParam  - camel case
# ctrl + r замена контекстная
# RAM random access memory  любое удобное кресло
# DRY Do Not Repeat yourself (code should be clean - код должен быть чистым)

dist = 120  # переменной dist присвоено значение 120
# sides = 8   # количество сторон многоугольника число сторон замкнутой фигуры
sides_of_figures = 8   # количество сторон многоугольника число сторон замкнутой фигуры
# in this case mistakes
# sides_of figures = 8   # количество сторон многоугольника число сторон замкнутой фигуры
#              ^^^^^^^
# SyntaxError: invalid syntax
# Process finished with exit code 1
angle = 360 / sides_of_figures # угол поворота черепашки

t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)

t.mainloop()