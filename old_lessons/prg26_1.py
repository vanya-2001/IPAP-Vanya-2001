 #  Примеры задач со мнодествами
 # создать пароль  в пароль входят
 # letter_set = {}
 # digit_set = {}
 # symbol_set = {}
forbidden = {'l', 'O', 'I'}
letter_set = {'a', 'b', 'c', 'd', 'l', 'O', 'I', 'j', 'w', 'z'}
digit_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 1. Удаляем некорректные символы
remove_incorrect = letter_set - forbidden
# 1а. Проверяю
# print(remove_incorrect)

# 2. Объединяю очищенное множество и цифры = итоговый set для пароля
temp = remove_incorrect | digit_set
# 2а. Проверяю - промежуточный результат
print(temp)
# 3. Задача составить и вывести на экран 5-ти значный пароль
temp = list(temp)
for i in range(0, len(temp), 4):
    print(temp[i], end='') # обратиться по индексу


