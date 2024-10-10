# Чтение нескольких строк (способ №1)

fo = open('sample.txt', encoding='utf8')
# print(dir(fo))

text = fo.readline()
while text: # если строка существует, то True
# while text  != '' - пустая строка
    print(text, end='')
    text = fo.readline()
else:
    print('\nусе')
fo.close() # открытый файл обязательно закрывать
# print(text)
#  text = fo.readline() Это первая строка внутри файла
#  text = fo.readlines()
# ['Это первая строка внутри файла\n', 'Это вторая строка внутри файла']


#['_CHUNK_SIZE', '__class__', '__del__', '__delattr__',
# '__dict__', '__dir__', '__doc__', '__enter__', '__eq__',
# '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable',
# '_checkWritable', '_finalizing',
# 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors',
# 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name',
# 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure',
# 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through',
# 'writelines']
