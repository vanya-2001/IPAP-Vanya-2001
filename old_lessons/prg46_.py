# Файлы (запись)
# name.ext
# Режимы ( mode) r - read, w - write, a - append
# b - binary, t -text

    #fo = open('sample.txt', 'wt') # по умолчанию  READ
fo = open('sample.txt', 'wt', encoding='utf8')
    # что можно сделать?
    # print(fo.name) # name() - недопустимо () - обращение к функции name
    # # result sample.txt
    # print(fo.mode) # result wt
    # print(fo.encoding) # utf8
# fo.read() # io.UnsupportedOperation: not readable
fo.write('Это текст внутри файла')
# num = fo.write() # arg - enpty в режиме write - все содержимое перезаписывается заново
# , поэтому result TypeError: TextIOWrapper.write() takes exactly one argument (0 given)

num = fo.write('Это текст внутри файла') # result 22 байта - символа, включая пробелы

print(num)
    # print(fo)
#    <_io.TextIOWrapper name='sample.txt' mode='wt' encoding='cp1251'> textIOWrapper - текстовая обертка
fo.close() # открытый файл обязательно закрывать