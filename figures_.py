# Классы фигур (наследование)
# Родительский (базовый) класс (superclass)
# Дочерний (производный, наследник) класс
from math import pi


class Restangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f'Это прямоугольник со сторонами {self.width}, {self.height}'
    # Getters
    def get_width(self):
        return self.width
    def get_heght(self):
        return self.height

    # Setters
    def set_width(self, new_w ):
        self.width = new_w

    def set_heght(self, new_h):
        self.height = new_h


    # перехват адреса оращения на сравнение сторон
    def __eq__(self, other):
        return self.width == other.width

    def __gt__(self, other):
        return self.side > other.side

    def __lt__(self, other):
        return self.side < other.side

    def __sub__(self, other):
        return Square(self.side - other.side)

    def __repr__(self):
        return f'Квадрат со стороной {self.side}'

    def __del__(self):
        print(f'Квадрат со стороной {self.side} стёрт!')


class Square(Restangle):
     def __init__(self, s=1):
        super().__init__(s, s)
        self.side = s




class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        # return self.radius * 2 * pi
        return round(self.radius * 2 * pi, 2)  # round округление


