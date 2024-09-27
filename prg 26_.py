# примеры задач со множествами

forbiden = {}
letter = {'a', 'b', 'c', 'd', 'l', 'I'}
digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# удаляем некорректные символы
remove_incorret = letter - forbiden
# объединяем с цифрами
temp = remove_incorret | digits

# print(temp)