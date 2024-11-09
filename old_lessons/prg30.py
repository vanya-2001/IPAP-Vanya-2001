# форматироование строк
# stackoverflow https://stackoverflow.com/
# %s - для подстановки str
# %d   - для подстановки int ( digit)
# %f - для подстановки float

name = "Виктор"
age = 9
heght = 141.5


# Placeholder Method

# f_string = "%11s,\nвозраст: %2d,\nрост: %5.1f см " % (name , age, heght )
#
# print(f_string)

# Format Method (позиционные аргументы и плейсхолдеры

# f_string = "Name :{N}, \nAge: {A} years old, \nheght:{H}".format(N=name, A=age, H=heght)
#
# print(f_string)
#
# f_string = "Name :{0}, \nAge: {1} years old, \nheght:{2}".format(name, age, heght)
# print(f_string)
#
# f_string = "Name: {:s}, \nAge: {:5d} years old, \nheght:{:.2f}".format(name, age, heght)
# print(f_string)

# String Method (интерполяция строк)
f_string = f"Name: {name}, Heght: {heght:.3f}, Age: {age}"
print(f_string)

f_string += f"При фигуре из 4-х сторон угол равен: {360/4}"
print(f_string)