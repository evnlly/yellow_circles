import sys
import random
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPaintEvent, QPainter, QColor
from PyQt6.QtCore import QRect
from PyQt6 import QtWidgets, uic, QtGui, QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(circle)

    def add_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        circle = QRect(x, y, diameter, diameter)
        self.circles.append(circle)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())