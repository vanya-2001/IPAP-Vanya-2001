string = 3 # int() float() bool - не-итеририуемые объекты,
# при этом input() - это строка введенная пользователем
#length = len(string) # WRONG
length = len(str(string))  # CORRECT
print(length)
"""
    length = len(string)
             ^^^^^^^^^^^
TypeError: object of type 'int' has no len()
"""

number = input('Введите целое положительное число: ')
# print('Пользователь ввел число: ', number, ', состоящее из ', len(number), 'разрядов')

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