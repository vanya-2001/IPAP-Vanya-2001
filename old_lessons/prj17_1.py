# ВВедение в цикл FOR
# Система трех с
# s - dtart (по умолчанию 0  значение включено)
# s - stop () не включая - отсчет с 0
# s - step (по умолчанию - 1)
# range(start, stop, step)  тольуо целые числа
# step только увеличение обратной последовательности нет

# вывести ряд четных чисел, начиная с 2 включая 22
"""
for x in range(2, 22, 2):
    print(x)
"""
"""
#  от 1 до 11 с шагом 2
for x in range(1, 13, 2):
    print(x) 
"""
# for <переменная> <в> <диапазоне> (начало, финиш, шаг):
#     выполнить ()
"""
for x in range(5):
    print('Привет! ')
"""
"""
# reverse
for g in reversed(range(1, 11)):

    print(g)
"""
"""
start = 1
stop = 10
step = 3
for g in reversed(range(start, stop, step)):
    print(g)
"""
# 1 способ
"""
# диапазьн от 1 до 50 (вкл)
for x in range(4, 51, 10):
    print(x)
"""

# 2 способ
for x in range(1, 51):
    if x % 10 == 4:
        print(x)
