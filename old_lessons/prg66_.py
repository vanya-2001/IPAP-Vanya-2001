# Импортирование классов
from figures_ import Square
# from figures_ import * сочетание клавиш Ctrl Alt O Optimize Import

if __name__ == '__main__':
    sq1 = Square(10)
    sq1.set_heght(125)
    print(sq1.get_width())
    print(sq1.get_heght())


    """
    
    sq2 = Square(6)
    complex_sq = [Square(2), Square(3)]

    sq1.set_heght(15)
    print(sq1)
    square = sq1 - sq2
    print(complex_sq)
    print(sq1 == sq2)
    """

  #  print(sq1 >= sq2)