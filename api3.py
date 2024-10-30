import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Мое приложение на Qt6')

        button = QPushButton('Кнопка')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setFixedSize(QSize(600, 400))
        #self.setMinimumSize(120,80)
        #self.setMaximumSize(1200,600)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)


    def the_button_was_clicked(self):
        print('Нажал на кнопку')

    def the_button_was_toggled(self, checked):
        print('Переключили?', checked)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()