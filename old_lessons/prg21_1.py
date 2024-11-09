# Управление циклом с помощью break  и continue
# break - безусловное прерывание цикла
# continue -  эту итерацию цикла пропустить, но продолжай выполнять цикл

# for x in range(5):
#     if x == 2:
#         continue
#     print(x)
#
# for x in range(5):
#     if x == 3:
#         break
#     # else:
#     #     continue ТАК ДЕЛАТЬ НЕЛЬЗЯ
#     print(x)
# else:
#     print('Нормальное завершение цикла')

# выведите элементы строки (буквы слова) без пробелов
string = 'О, сколько2!'

# for x in string:
#     if x == 'о' or x == 'О':
#         continue
#     print(x, end=' ')
# for x in string:
#     if x == ' ':
#         continue
#     print(x, end='')

for x in string:
    if x == '2':
        break
    print(x, end='')