# Обработка исключений
 # Деление на ноль и проч

 # try (начало обработки)
# выполняется попытка какого либо действия
 # EXCEPT (обработка исключения)
 # FINALLY (необязательно) программа продолжается
# с этого места независимо было исключение или нет
# ELSE Если не было исключений
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
    #except ZeroDivisionError:
     #0
    # return 'Делить на ноль нельзя!'
    #except ValueError:
     #   return 'Пожалуйста вводите только числа'
    except Exception as excp:  # так делать не очень рекомендуется
        return f'Вот такое вот  исключение   {excp }'


res = divide()
print(res)
