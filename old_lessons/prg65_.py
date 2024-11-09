# Объектно-ориентированный подход
# Спецметоды (operators overloading, overriding)

class Square:
    def __init__(self, s=1):
        self.side = s
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return self.side * 4
    # Перехват вывода строки принтом своей записью
    def __str__(self):
        return f'Это квадрат со стороной {self.side}'
    # перехват адреса оращения на сравнение сторон
    def __eq__(self, other):
        return self.side == other.side

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



sq1 = Square(5)
sq2 = Square(4)

sq1 = Square(10)
sq2 = Square(6)
complex_sq = [Square(2), Square(3)]

print(sq1 == sq2) # False Адреса в памяти не равны
print(sq1 > sq2)
print(sq1 < sq2)