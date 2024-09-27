# 4 вида коллекций кортежи списки множества словари #все коллекции итерируемые
#   множества - set()
#   списки  - list() ->  []
#   кортежи - tuple() - > ()
#   словари     - dictionary dict() -> {}


# МНОЖЕСТВА  - неупорядоченное структура ланных
#   Множество не содержит повторов !!
empty_set = set() #чтобы создать пустое
error_method = set("1, 2, 4, F")
num_set = {1,2,3, "строка", 36.6,  False, True } # нет ограничений по наполнению
#
print(num_set)

num_set = {1, 2,3}
print(num_set)
letter_set = {'a', 'b', 'c', 'b', 'b'}
# метод добавления данных
letter_set.add('d')
letter_set.add('7')
# метод удаления данных .pop случайное удаление элементов
letter_set.pop()
letter_set.remove("у") # метод удаления данных .remove  удаление конкретного элемента с проверкой
letter_set.discard("a") # удаление в слепую
print(letter_set)

word = "молоток"
if 'о' in word:
    print('Да')
letter_in_word = set(word)
print(word)

