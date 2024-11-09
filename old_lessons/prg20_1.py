# как узнать количество итерируемых объектов?
# len()  # функция -  определение числа элементов в итерируемом объекте

# string = 'Телеелевидение'


number = input('Введите целое положительное число: ')
# мое
#  item = 0
#  for _ in number:
#      item = item + int(_)
#  print(item)

# мое 2
# item = 0
# for _ in number:
#     item += int(_) # модиыикация
# print(item)
# total = 0
# for item in number:
#     total += int(item)
# print('Сумма разрядов числа', number, 'равна', total)

# произведение разрядов числа
item = 1
for _ in number:
    item *= int(_) # модиыикация
print('Произведение разрядов числа', number, 'равна', item)

# total = 0
# for item in number:
#     total += int(item)
# print('Сумма разрядов числа', number, 'равна', total)


# print('Пользователь ввел число: ', number, ', состоящее из ', len(number), 'разрядов')
"""
if len(number) == 1:
    print('Число', number, 'одно-значное')
elif 1 < len(number) <= 4:
    #  print('Число ', number, ' - ', len(number), '-х значное', sep='') # мой вариант
    #    print('Число ', number, ' - ', len(number) + '- х',  'значное')  # MANWELL 1

    #   print('Число ', number, ' - ', len(number) + '-х',  'значное')  # MANWELL
    #                                  ~~~~~~~~~~~~^~~~~~~
    #    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    #    попытка конкатенировать число и строку

    print('Число ', number, ' - ', str(len(number)) + '-х',  'значное')  # MANWELL 2 CORRECT
elif len(number) > 4:
    print('Число ', number, ' - ', len(number), '-ти значное', sep = '')
"""

"""
    length = len(string)  # функция -  определение числа элементов в итерируемом объекте
    
    print('В слове', string, length, 'символов. ')
"""
"""
    for i in range(5):
        pass #TODO
    for _ in range(5): # если переменная не используется в дальнейшем
        print('Привет! ')
"""
