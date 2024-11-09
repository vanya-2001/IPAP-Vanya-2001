# Форматирование строк
# placeholders
# %s - для подстановки str
# %d - для подстановки int (digit)
# %f fljt
name = 'Виктор'
age = 9
height = 141.56 # округляет

# Placeholders method
"""
f_string = '%11s, \nвозраст: %2d, \nрост: %5.1f см' % (name, age, height)
print(f_string)
"""

# Fornat method {named args}

# f_string = ('\tИмя: \t {N},\n\tвозраст: \t {A} \tлет, \n\tрост: \t {H}\tcm '.format(N=name, A=age, H=height))
# print(f_string)

# Fornat method {positioned args}
"""
f_string = ('\tИмя: \t {0},\n\tвозраст: \t {1} \tлет, \n\tрост: \t {2}\tcm '
            .format(name, age, height))
print(f_string)
"""
 # Fornat method {positioned args and placeholders}
"""
f_string = ('\tИмя: \t {:s},\n\tвозраст: \t {:d} \tлет, \n\tрост: \t {:.1}\tcm '
            .format(name, age, height))
print(f_string)
"""
# Fornat method f-string = f'' STRING INTERPOLATION
n = 10
f_string = f'Имя: {name}, Возраст: {age}, Рост: {height}'
f_string += f'\nВнутренний угол фигуры из {n:12} сторон будет: {360 / n}'
print(f_string)