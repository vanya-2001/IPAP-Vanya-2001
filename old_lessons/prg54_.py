# Функции (encapsulation - инкапсуляция)
# Область видимости переменных
# Global scope
b = 5
c = 15


def calc(x: int = 1, y: int = 0) -> int:
    # local scope
    # b = 3 # так допустимо внутри функции, интерпретаор возьмет это щначение
    # но только внутри
    res = 2 * x + y + b  #  промежуточные переменная
    # x y res    не видны вне области функции и после вычислений стираются из памяти

    return res


def increment():
    global b
    b += 1
#    return (b) нихт арбайтен
# в данной ситуации return не используется,
# так ка произошло вычисление по глобальной переменной

def multy(*args: int) -> int:
    """
    Функция вычисления переменного числа аргументов
    :param args: ноль или несколько целых
    :return: произведение аргументов
    """
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]
    res = 1
    for i in range(len(args)):
        res *= args[i]
    return res


print(multy(1, 2, 8, 5))

increment()  # вызов = отработка
result = calc()
# garbage collection - сборщик мусора - удаляет из памяти все неиспользуемые переменные
print(result)
