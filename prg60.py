# Задача на использование исключений
# точное соответствие заданмю не выполнено, отложено на потом
while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    try:
        a = int(a)
        b = int(b)
        c = a / b
    except ValueError:
        print('Необходимо вводить только числа.')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    else:  # исключений не возникало
        print(c)
        break