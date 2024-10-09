# Методы списков и строк
# print(dir([])) вывести меды списка print(dir('')) вывести методы строки
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
additional = ['колбаса', 'редис', 'картофель']

final = okroshka + additional + ['петрушка']
final.append('укроп')  # final += ['укроп']
# Способ №3 Конкатенация списков
print('Ингредиентов в окрошке:', len(final))
print('Вот они: ', end='')
final.sort() # список изменяемая последовательность -->
# его можно поменять на месте, то есть применить метод или функцию,
# не выполнять никаких прсвоений это рсрбенность изменяемых типов данных

final.sort() # Ничего не возвращает None
print('\t', *final, sep='\n\t')
# Ингредиентов в окрошке: 10
# Вот они:
# 	картофель
# 	квас
# 	кефир
# 	колбаса
# 	огурец
# 	перец
# 	петрушка
# 	редис
# 	соль
# 	укроп

s = 'Сабака' # строка неизменяемый тип данных,
# уогда мы ее меняем ны обязаны выполнить присвоение результата новой строке

n = s.replace('а','о', 1)
print(n)