# Дано код без обработки исключений
while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        res = int(a) / int(b)
        print(f'Результат деления первого числа {a} на второе {b} равен {res}')
        break
        #if not a.isdigit() and b.isdigit():
    except ValueError:
        print('необходимо вводить только числа')
        #if int(b) == 0:
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
         #   if int(b) == 0:
        #res = int(a) / int(b)
        #print(res)




"""
    if a.isdigit() and b.isdigit():
        if int(b) == 0:
            print('Делить на ноль нельзя!')
        else:
            print(int(a) / int(b))
            break
    else:
        print('необходимо вводить только числа')
"""