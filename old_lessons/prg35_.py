import string as s
import random as r

num = 8
# назначили переменную количества символов в пароле

set_of_symb  = s.digits + s.ascii_lowercase + s.ascii_uppercase
# создали СТРОКУ - набор символов

set_of_symb = set(set_of_symb)
# Строка в Множество

set_of_symb = set_of_symb - {'0', 'O', '1', 'l', 'I'}
# Удалили неправильные сомнительные символы

set_of_symb = list(set_of_symb)
# Множество в ЛИСТ конвертируем в список

r.shuffle(set_of_symb)
# Перемешали символы в листе списке

# # 1 способ срез
# temp = set_of_symb[:num]
# # лист список из первых символов пароля количеством символов = n
# pswrd = ''.join(temp)
# # объединяем все символы списка в строку
#
# print(pswrd) # TpRQxbHw
# # вывод

# # 2 способ
# temp = set_of_symb[:num]
#
# temp += ['#', '&', '@', '?', '$']
# # добавили спецсимволы
# r.shuffle(temp)
# # перемешали еще раз
# pswrd = temp[:num]
# # создаем пароль нужной длины список из первых символов  = n
#
# pswrd = ''.join(pswrd)
# # объединяем все символы списка в строку
#
# print(pswrd) # &#a?wX$V #&ft@NW7 c#$o4@&6
# # вывод

# # 3 способ случайные n символов
# temp = [r.choice(set_of_symb)]
# # назначили переменнцю случайнм выбором из списка
# for _ in range(num):
#     temp.append(r.choice(set_of_symb)) # !это уже список строка 55 не нужна
#     # temp += r.choice(set_of_symb)
#
# # # получили строку из n символов
# # temp = list(temp)
# # конвертировали строку в список
#
# temp += ['#', '&', '@', '?', '$']
# # добавили спецсимволы
# r.shuffle(temp)
# # перемешали еще раз
# pswrd = temp[:num]
# # создаем пароль нужной длины список из первых символов  = n
#
# pswrd = ''.join(pswrd)
# # объединяем все символы списка в строку
#
# print(pswrd) # WR@&t9EE uJ$A#D&4 4c56$yqr
# # вывод

# 4 способ метод sample случайная выборка из списка в виде списка без повторов
temp = r.sample(set_of_symb, k = num)
print(temp)

temp += ['#', '&', '@', '?', '$']
# добавили спецсимволы
r.shuffle(temp)
# перемешали еще раз
pswrd = temp[:num]
# создаем пароль нужной длины список из первых символов  = n

# проверяем, что спец. символ не стоит на 1-м месте
while temp[0] in ['@', '!', '#', '$', '&', '?']:
    r.shuffle(temp)

pswrd = ''.join(pswrd)
# объединяем все символы списка в строку

print(pswrd) #
# вывод

# help(r.sample)
# Help on method sample in module random:
#
# sample(population, k, *, counts=None) method of random.Random instance
#     Chooses k unique random elements from a population sequence.
#
#     Returns a new list containing elements from the population while
#     leaving the original population unchanged.  The resulting list is
#     in selection order so that all sub-slices will also be valid random
#     samples.  This allows raffle winners (the sample) to be partitioned
#     into grand prize and second place winners (the subslices).
#
#     Members of the population need not be hashable or unique.  If the
#     population contains repeats, then each occurrence is a possible
#     selection in the sample.
#
#     Repeated elements can be specified one at a time or with the optional
#     counts parameter.  For example:
#
#         sample(['red', 'blue'], counts=[4, 2], k=5)
#
#     is equivalent to:
#
#         sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)
#
#     To choose a sample from a range of integers, use range() for the
#     population argument.  This is especially fast and space efficient
#     for sampling from a large population:
#
#         sample(range(10000000), 60)


