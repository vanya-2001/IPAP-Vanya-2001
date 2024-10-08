# От строк к спискам и наоборот
a = ['огурец', 'квас', 'перец', 'колбаса',
     'кефир', 'редис', 'картофель', 'петрушка', 'укроп']
b = a[:3]
#
# b.sort()
# print(b)
# # Вывод списка строкой (способ №1)
# print(*b, sep=',') # НАЗНАЧАЕМ ЕГО СТРОКОЙ <*b>

# Вывод списка строкой (способ №2: из списка в строку)
# задача не вывести на принт, а присвоить переменной строку их списка b
res = ', а еше '.join(b)
print(res)

word = 'pitton'

lst = list(word)
lst[0] = 'P'
lst[1] = 'y'
lst[3] = 'h'
print(''.join(lst))


# help(''.join)
# join(iterable, /) method of builtins.str instance
# print(''.join(lst))
# Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'