# Сложное  условие ЛОГИЧЕСКОЕ "ИЛИ"
# ПРИРИТЕТ AND (логическое умножение) затем OR (логическое сложение)
# 3 + 2 * 5  (3+2) * 5
stribg = ''  # пустая строка

name = input('Как Ваше имя: ')
surname = input('Как Ваша фамилия: ')
# Дополнительное условие
if name == 'Вася' and surname == 'Пупкин' :
    print('Досвидос ' + name + ' ' + surname + '!' '\n' + 'Попробуйте еще раз!' )
else:

    age = input('Ваш возраст: ')
    gender = input('Укажите свой пол (М или Ж): ')


    # Это Основоное условие
    # if gender == 'М':
    if (gender == 'М' or gender == 'м' or gender == 'V' or gender == 'v'):
        stribg = 'Уважаемый '
    if (gender == 'Ж' or gender == 'ж' or gender == ':' or gender == ';'):
        stribg = 'Уважаемая '
    else:
        stribg = 'Уважаемый товарищ '
    # #######

    print(stribg + '\t' + name + ' ' + surname + '!'
          + ' \nВаш возраст ' + age + ' годков.')
