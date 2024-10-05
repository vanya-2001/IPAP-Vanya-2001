# Стандартный вывод (stdout) - в консоль (orint)
# именованые аргументы:  sep='<пробел> " и end='\n' <новая строка>
# Стандартный вывод (stdin) - c клавиатуры (input)
# Когда внутри функции пишем именованые аргументы и их значения
# значок = не выделяется пробелами PEP8
# flush=False не очищать поток консоли  flush=True - очистить
# print('Строка 1')
# print('Строка 2')
#
# print('Строка 1', 'Строка 2')
"""
Help on built-in function print in module builtins:
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
"""

#print('Строка 1', 'Строка 2', sep=' и ')
#print('Строка 1', 'Строка 2', 'Строка 3', sep=' -> ')
# print('Строка 1', 'Строка 2', 'Строка 3', sep=' -> ', end='. \n ---')
#
# print('Новая строка')

#print('И смех','слезы','любовь', sep=', и ',end='. \n')

# Приложения исполmзуюшие только консоль для вывода называются консольными

print('Сегодня в меню:', 'суп', 'пюре', "компот", sep='\n\t- ')

num = 16
print('А' + 'у'*num + "!")

print('А', end='')
for i in range(num):
    print('у', end='')
#    i = i +1 # 'этот шаг не нужен
print('!', end='\n')

# num = 16
print('А', end='')
while num > 0:
    print('у', end='')
    num = num - 1
print('!', end='\n')


