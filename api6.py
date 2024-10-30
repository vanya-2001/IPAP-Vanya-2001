import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


from random import choice

window_titles = [
    'Мое первое приложение',
    'Мое  приложение',
    'Пока еще мое первое приложение',
    'Пока еще мое ',
    'Что в мире делается',
    'What on earth',
    'Это сюрприз!',
    'Это сюрприз!',
    'Что-то пошло не так'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle('Мое первое приложение на Qt6')

        self.button = QPushButton("Кнопка, чтобы надавливать на мышку!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setFixedSize(QSize(600, 400))
        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == 'Что-то пошло не так':
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()