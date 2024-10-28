# создать класс описывающий человека, возраст и имя
class Man:
    def __init__(self, name='Вася Пупкин', age=21):
        self.name = name
        self.age = age
    def info(self):
        print('У человека по имени ', self.name, 'возраст ', self.age)

mam1 = Man()
man2 = Man('Василий Иванович', 42)
mam1.info()
man2.info()