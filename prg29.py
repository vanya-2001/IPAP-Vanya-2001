# Основные методы строки

s = 'Телевидение'

# print(s.lower()) # Все буквы маленькие
# print(s.upper()) # Все буквы большие
# print(s.cspitalize()) # First letter first word
# print(s.title()) # Allfirdt letters in word - CAPS
# print(s.strip()) # удаляет символы заключенные в скобках слева и справат со строки перед и после пробелы - без аргументов - пробел
# print(s.strip()) # снимает со строки перед и после пробелы - без аргументов
# print(s.lstrip()) # l - left r- rights
# print(s.lstrip("n").lower()) # цепочка вызовов
# print(s.count('е', 4))

print(s.index('ви'))  # индекс по символу