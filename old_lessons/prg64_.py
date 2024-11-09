# Объектно-ориентированный подход
# Полиморфизм метод который выполняется по принадлежности к классу
#import math
from math import pi




class Square:
    def __init__(self, s):
        self.side = s
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return self.side * 4


class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * pi

    def perimeter(self):
        # return self.radius * 2 * pi
        return round(self.radius * 2 * pi, 2) # round округление

class Restangle:
    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def area(self):
        return self.side_a * self.side_b

    def perimeter(self):
        return (self.side_a +self.side_b) * 2



circle =Circle(5)
square = Square(6)
rest1 = Restangle(5,7)
#print(circle.perimeter())
#print(square.perimeter())
print(rest1.perimeter())
print(rest1.area())

if circle.__class__.__name__ == 'Circle':
    print(f'Это экземпляр класса {Circle}')
else:
    print(f'Это экземпляр класса {circle.__class__}')

#if rest1.__class__.__name__ == 'Circle':
#    print(f'Это экземпляр класса {Circle}')
#else:
#    print(f'Это экземпляр класса {circle.__class__}')
