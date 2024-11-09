# Обработка исключений
# Деление на ноль и проч
# var 2 мой

def divide():
    a = input('Введите A: ')
    b = input('Введите B: ')
    try:
        temp =  float(a) / float(b)
        return temp
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    except ValueError:
        return 'Пожалуйста вводите только числа'

res = divide()
print(res)
