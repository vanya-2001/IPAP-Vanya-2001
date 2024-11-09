# Виды коллкций в  PYTHON (iterable collection)
# 1. Множества  - set()     -> set() пустое множество задаем только так > {x, w. z}
# 2. Списки     - list()    -> [] пустой кортеж                         >  [}x, w. z]
# 3. Кортежи    - tuple()   -> () пустой спиcок
# 4. Словари    - dict()    -> {} пустой словарь


# empty_set = set()  # пустое множество
# num_set = {1, 2, 3, 'строка', 36.6, True, False }

# неупорядоченная структура данных, неупорядоченная коллекция
# Мнодество не содержит повторов

num_set = {1, 2, 3} # для целых чисел порядок сохраняется
print(num_set)
letter_set = {'a', 'b' ,'c', 'd', 'e'}
letter_set.add('d') # добавление в множество
letter_set.add('a')
print(letter_set)


# 1 способ сслучайное удаление
# letter_set.pop() # случайное удаление аргумента no arguments

# 2 способ с проверкой
# letter_set.remove('a') # удаление конкретного элемента из множества, но с проверкой
# letter_set.remove('r') # KeyError: 'r'

# 3 способ без проверки
letter_set.discard('y')
letter_set.discard('e')
print(letter_set)

# error_method = set(1,2,3) # TypeError: set expected at most 1 argument, got 3
error_method = set('1,2,3') # {'1', '2', ',', '3'}
# error_method = set('1, 2, 3, 3 ') # {'2', ' ', ',', '1', '3'}
print(error_method)

# word = 'молоток'
#
# letter_in_word = set(word)
# print(letter_in_word)
# # есть ли буква о в слове молоток
# if 'о' in word:
#     print('есть буква о в слове')
#
# # {False, 1, 2, 3, 36.6, 'строка'}




 #  чтобы превратить в строку str()