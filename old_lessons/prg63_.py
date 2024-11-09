# создать класс описывающий человека, возраст и имя
# Объектно-ориентированный подход
# Инкапсуляция
# 3 модификаора доступа
# private __ два подчеркивания в начале self.__name
# public
# protected _ self._name одно подчеркивание в начале
class Man:
    # Спец. методы
    def __init__(self, name='noname', age=0):
        #name='noname', age=0 наверно правильно умолчание делать так быстрее
        self.name = name
        self.age = age
        self.non_legal_names = ['Васёк', 'Павло', 'Павлик', 'Ванька', 'Машка']
    def info(self):
        #print('У человека по имени ', self.name, 'возраст ', self.age)
        print(f'У человека по имени  {self.name} возраст  {self.age} лет, ну или годов')

        # Сеттеры (setters)
    def set_age(self, new_age):
        if new_age < 0:
            self.age = - new_age
        else:
            self.age = new_age
    def set_name(self, new_name):
        if new_name not in self.non_legal_names:
            self.name = new_name
        else:
            print('Низя такое имя')

    # Геттеры (getters)
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    # метод  вывода списка запрещенных имен
    def print_non_legal_names(self):
        print(*self.non_legal_names, sep=', ')


man1 = Man('Петька', 33)
dima = Man('Дмитрий', 17)
man2 = Man('Василий Иванович', 42)

# dima.age(18)  #  так некорректно
dima.set_age(-18) #  так корректно, так как есть проверка идет
man1.set_name('Ванька')


man1.info()
man2.info()
dima.info()