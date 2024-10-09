# Словари
# d = dict()  # пустой словарь
# d = {}  # пустой словарь

d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple',
    'меню': ['суп', 'тефтели', 'чай'],
}
d['слива']  = 'plum'
d[0] = ('one')
d[36.6] = 'normal'
d[True] = 'Истина'
print(len(d))
print(d.keys()) #   список всех ключей словаря dict
print(d.values()) #   список всех ключей значений dict
print(list(d.items())) # список кортежей
for key in d: # for key in d.key()):
    print(f'Ключ: \t{key} : Значение: {d[key]}')

# ! По  значению перейти к ключу НЕЛЬЗЯ
# Но мы можем спросить есть ли такое значение

if 'слива' in d:
    print('Слива есть среди ключей')

if 'Истина' in d.values():
    print('Истина есть среди значений')

for key, value in d.items():
    if value == 'normal':
        print(f'{key}: {value}')
# for key in d.keys():
#     if 'plum' in d.values():
#         print(f'Ключ: \t{key} : Значение: {d[key]}')
# # print(d)

print(d.get('груша', False))
del d['стул']
print(d)
# print(d['стол'])


# print(dir(d))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__',
# '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
# '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop',
# 'popitem', 'setdefault', 'update', 'values']