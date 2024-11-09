# import turtle as t  # подключили "черепашку"
choice = ''  # инициализация выбора пользователя
yes_no = " "

while choice != 'q':
    choice = input('Вы на развилке. Введите r, если хотите пойти направо '
                   'или l, если налево. Если надоело q: ')
    if choice == 'r':
        print('Повернули направо', choice)
    elif choice == 'l':
        print('Вы повернули налево', choice )
    elif choice == 'q':
        print('Надоело?')
    else:
        print('Моя шайтан-арба твоя язык не понимает: ', choice)
print('До свидания!')