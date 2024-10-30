import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox,  QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(600, 400))
        #widget = QLabel("1")  # Создана метка с текстом 1.
        #widget.setText("2")  # Создана метка с текстом 2.

        widget = QLabel("Hello")
        #widget.setPixmap(QPixmap('otje.jpg'))
        font = widget.font()
        font.setPointSize(100)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()