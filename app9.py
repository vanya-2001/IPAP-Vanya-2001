import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setFixedSize(QSize(600, 400))


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.label.setText('mousePressEvent LEFT')

        elif e.button() == Qt.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.label.setText('mousePressEvent MIDDLE')

        elif e.button() == Qt.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.label.setText('mousePressEvent RIGHT')

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()