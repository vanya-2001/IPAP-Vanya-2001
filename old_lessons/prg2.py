import turtle as t  # подключили черепашку

# prg_1.py - snake case
# prGramm1.py camel case
# t. point насадка извлечение
# RAM - random accsess memory - любое свободное место
# DRY - Do not repeat yourself ( code should be clear)

sides = 8  # число сторон замкнутой фигуры
dist = 50  # переменной присвоено значение 200
angle = 360 / sides  # угол, как 360  /  ides


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

t.mainloop()
