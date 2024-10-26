# Обработка исключений
 # Деление на ноль и проч
# var 1 мой
"""

"""
def divide():
    """
    
    :return: 
    """
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        return a / b
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    except ValueError:
        return 'Пожалуйста вводите только числа'


res = divide()
print(res)
