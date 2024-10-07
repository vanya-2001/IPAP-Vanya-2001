# Основные методы строки

#  s = 'яяяяяяяяяяяяяяяЯзык программирования PyThonяяя'
# s = ('Телевидение' )
"""
print(s.count('е', 2, 6))
print(s.lower()) # lower case
print(s.upper()) # upper case
print(s.capitalize()) # Case Sentebse
print(s.title())    # all caps
print(s.strip('я'))  # удаляет все символы в скобках слева и справа. по умолчанию пробел
print(s.strip('я').lower())
print(s.count('е')) # подсчет кол-ва
print(s.index('еви')) # индекс по символу илди первое вхождение
print(s.find('е')) # -1 ничего не найдено
print(s.find('е', 2))
print(s.rfind('е')) # 10 возвращает номер последнего вхождения
"""
s = ('Тиливидение' )
print(s.replace('и', 'е',2)) # замена подстроки
print(s.startswith('Тили')) #true False
print(s[0:4])
# if s.startswith('Тили'): # if s[0:4] == 'Тили'
#     pass

# res = input(' Введите: '.strip().lower()) # подготовка палиндрома для проверки


