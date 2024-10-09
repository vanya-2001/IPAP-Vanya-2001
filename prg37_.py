# Методы списков и строк
# print(dir([])) вывести меды списка print(dir('')) вывести методы строки
#  как можно разбить строку на отдельные части, а потом собрать и для чего это нужно
# text = 'О  сколько нам открытий чудных' # разбить на слова

# слова без повторений
# по алфавиту
# слова не короче 2-х символов >2
#   Частотный анализ строк
text = 'О сколько   нам открытий чудных О   сколько нам открытий чудных'

lst = text.split()  # ' ' по разделителю
# Сколько раз встретилось слово "сколько" до того как мы убрали повторы
print('Слово "сколько" повторилось ', lst.count('сколько'), ' раз(a).')
print(f'Слово "сколько" повторилось  {lst.count('сколько')}  раз(a).')
# count = lst.count('сколько')
# print(f'Слово "сколько" повторилось {count} раз(а).')
set_lst = set(lst)  # обратили в множество = убрали пробелы
lst = list(set_lst)  # обратили в список


str_lst = ' '.join(lst)
print(str_lst)
str_lst = str_lst.lower()
print(str_lst)
lst = str_lst.split()

lst.sort()
print(lst)

for word in lst:
    if len(word) <= 2:
        lst.remove(word)

for word in lst:
    if len(word) > 2:
        print('\t', word)
print('\t', *lst, sep='\n\t')

# print(dir([]))
# ['__add__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__',
# '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort']

# возвращает список


# print(dir(''))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__',
# '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__',
#  'capitalize', 'casefold', 'center', 'count',
# 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', # 'index', 'isalnum', 'isalpha',
# 'isascii', 'isdecimal', 'isdigit', # 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace',  'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
# 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
# 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
