from os import write


def f_open(name: str) -> str:
    """
    читает текстовый файл и возвращает его содержимое
    :param name: имя файла на чтение
    :return: содержимое файла
    """
    try:
        with open(name, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f'Файл не существует или удален'

print(f_open('example.txt'))
res = f_open('clever.dict')
print(res)

# НО сначала проверяется наличие файла
def f_open2(name: str) -> str:
    """
    читает текстовый файл и возвращает его содержимое
    :param name: имя файла на чтение
    :return: содержимое файла
    """
    try:
        with open(name, encoding='utf-8') as f2:
            return f2.read()
    except FileNotFoundError:
        with open(name, 'w', encoding='utf-8') as f2:
            f2.write('файл был заново создан')
        return f'Файл {name} не существует или удален'


print(f_open2('example.txt'))
# res = f_open2('clever.dict')
# print(res)
#  либо сохранить в переменную res = f_open('clever.dict')