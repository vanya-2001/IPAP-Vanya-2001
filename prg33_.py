# # Операции со списками и методы списков
# # print(dir([]))
# okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
# additional = ['колбаса', 'редис', 'картофель']
#
# final = okroshka + additional +  ['петрушка']
# final.append('укроп') # final += ['укроп']
# # count = 1
# # for i in final:
# #     print(f'\t{count}.\t {i}')
# #     count += 1
# # print(final)
#
# # Способ №2
# # print('Ингредиентов в окрошке:', len(final))
# # print('Вот они:')
#
# # for item in range(len(final)):
# #     print(f'{item + 1}. \t\t{final[item]}')
#


# методы списков
# print(dir([]))
# ['__add__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__delitem__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__iadd__',
#  '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__',
#  '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
#  '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
#  '__str__', '__subclasshook__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove',  'reverse', 'sort']
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
additional = ['колбаса', 'редис', 'картофель']
final = okroshka + additional +  ['петрушка']
final.append('укроп')
# final.sort()
# print(final.pop(6))
# final.pop()
# final.remove('квас')

#
# help([].sort())
# help([].insert())
x = 'кефир'
# final.insert([2], x)
temp = final.pop(3)
final.insert(len(final) - len(final), temp)
print(final)
# print(final.index(temp))
# final.clear()
final2 = final.copy().pop(4)
print(final2)
# Способ №3
print('Ингредиентов в окрошке:', len(final))
print('Вот они:')
# final.sort()
print(*final, sep='\n')
# print(final) #