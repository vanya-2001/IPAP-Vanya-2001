# Файлы (чтение
# name.ext
# Режимы ( mode) r - read, w - write, a - append
# b - binary, t -text

    #fo = open('sample.txt', 'wt') # по умолчанию  READ
fo = open('sample.txt', 'rt', encoding='utf8')
print(fo.name, fo.mode, fo.encoding)
#   text = fo.read() # по умолчанию () читает всеь файл до конца
#   text = fo.read(5) # result Это т 5  символов
    # # Как читает ридер -  fo.read(4) - читает первые 4 символа, но команды не было  и никуда не сохранил
    # fo.read(4)
    # # Как читает ридер -  fo.read(5) - итает следующие 5 символов и присваиват переменной text
    # text = fo.read(5)    # result текст
    # print(text)

    # fo.read(10)
    # text = fo.read(6)
    # print(text) # result внутри
text = fo.read()

print(f'Внутри файла "sample.txt" есть текст : {text}')
lst = text.split()
    # print(fo)
#    <_io.TextIOWrapper name='sample.txt' mode='wt' encoding='cp1251'> textIOWrapper - текстовая обертка
    # fo.close() # открытый файл обязательно закрывать
    # lst = text.split()
    # print(lst[3]) # return файла 3 element in list lst
    # print(lst) # ['Это', 'текст', 'внутри', 'файла']
    # for _ in lst:
    #     print(_)
# как извлечь нужный фрагмент из текста (способ №1)
    # if 'внутри' in lst:
    #     for word in lst:
    #         if word == 'внутри':
    #             print(word)
    # else:
    #     print('Такого слова в файле нет')

# как извлечь нужный фрагмент из текста
# метод списка индекс  (способ №2)
if 'внутри' in lst:
    indх = lst.index('внутри') # Присваиваем переменной indх значение индекса элемента внутри в списке lst
    print(lst[indх]) # выводим элемент с нужным индексом
else:
    print('Такого слова в файле нет')
