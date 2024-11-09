# Списки - iterable object, mutable-изменяемый тип коллекции

s = {'a', 1, 36.6}  # множество
empty_set = set()
array = []  # пустой список
array = list()  # пустой список
# index     0         1        2
array = ['ясно', 'пасмурно', '36.6']

# print(array[2][3])
# print(array[::2])

okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
#
# print(okroshka[0:len(okroshka):2])  # [::2]
# print(okroshka[-4::-1])

word = 'pitton'  # immutable
# word[1] = 'y' - так нельзя
lst = list(word)

# print(lst)

lst[1] = 'y'
lst[2] = ''
print(''.join(lst))

# wlst = ''.join(lst)
# print(wlst)


print(*lst, sep='')


dishes = ['борщ', 'пюре', 'компот', 'сок']
first, *sec, last = dishes
print(sec)
# first, second, third = dishes
# first, second, *drink = dishes
# *eat, compot, drink = dishes
# print(drink)
# sup = ''.join(dishes[0])
# print(sup)
for i in range(len(dishes)):
    print(''.join(dishes[i]))

