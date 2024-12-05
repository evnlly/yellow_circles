from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QPaintEvent
from PyQt6.QtCore import QRect
import random
from PyQt6 import uic
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.circles = []

    def run(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        circle = QRect(x, y, diameter, diameter)
        self.circles.append(circle)
        self.update()

    def paint(self, event: QPaintEvent):
        painter = QPainter(self)
        pen = QPen(QColor("yellow"), 2)
        painter.setPen(pen)
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())