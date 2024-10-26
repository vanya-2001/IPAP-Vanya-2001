# Утверждение (assertion)
# Утверждения для разработчика, а исключения для пользователя
length = 7
try:
     text = input(f'Введите любой текст, но не менее {length} символов: ')
     assert len(text) > length #  утверждение = требование
     print(f'Вы ввели  {text}, и оно состоит из {len(text)} символов,')
except AssertionError:
    print(f'нет, ваш текст {text} состоит из {len(text)} символов,'
          f' и он короче {length} cимволов')