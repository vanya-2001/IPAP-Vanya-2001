# строгая типизация  - сильная типизация
# взаимодействие возмодно только между данными (объектами) одного типа
# a = '4' # объект - тип данных
# print(type(a))

"""
a = 4 # объект - тип данных
b = 3
res = a - b # взимодействие между однии типом двнных (int) and (int)
# - + /  //  - не арифметические / математические операции, а операции взаимодействия
# 1  Process finished with exit code 0
"""

"""
a = 4.1
b = 3
res = a - b
print(res)
#   1.0999999999999996 #  Process finished with exit code 0
"""

"""
a = '4.1'
b = 3
res = a - b
print(res)
# File "D:\!!! !Python\IPAP vanya-2001\IPAP-Vanya-2001\prg4_1.py", line 23, in <module>
#     res = a - b
#           ~~^~~
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
# 
# Process finished with exit code 1
"""

"""
# особенность python - резкльтатом деления (int) всегда будет (float)
a = 4
b = 2
res = a / b
print(res)
# 2.0
#
# Process finished with exit code 0
"""

"""
a = 4
b = 2
res = a * b
print(res)
"""

"""
# строка на число умножается !!
a = '4'
b = 2
res = a * b
print(res)
# 44
# По сути это та же конкатенация одной строки, повторенная n раз
a = 4
b = '2'
res = a * b
print(res)
# 2222
"""
"""
a = '4'
b = 2
res = a + b # конкатенация строк - соединение
print(res)
#     res = a + b
#           ~~^~~
# TypeError: can only concatenate str (not "int") to str
"""
# a = '4'
# b = '2'
# res = a / b # eq. - * TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print(res)
