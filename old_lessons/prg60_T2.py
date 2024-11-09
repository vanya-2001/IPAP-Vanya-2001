while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        if a.isdigit() and b.isdigit():
            try:
                if not int(b) == 0:
                    pass
            except ZeroDivisionError:
                print('Делить на ноль нельзя!')
        pass
    except ValueError:
        print('необходимо вводить только числа')
    else:
        print(int(a) / int(b))


    """
    
    else:
        print('необходимо вводить только числа')
        
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

