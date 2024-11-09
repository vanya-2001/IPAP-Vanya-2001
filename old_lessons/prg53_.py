# Функция
def odd_even(num: int) -> str: # анотирование функции
    """
    Чет или Нечет
    :param num: Целое число
    :return: строка "Чет" или "НЕчет"
    """
    #if isinstance(num, (str, float)):
    # или сделать проще
    if not isinstance(num, int): # если int = True, то NOT TRUE = FALSE ->  'Сбрендил шо ли?'
        return 'Сбрендил шо ли?'
    if num % 2:
        return 'Нечет'
    return 'Чет'


# Вызов
res=odd_even(5)  # в случае прописания (num: int) - Pycharm будет "помогать№
print(res)
