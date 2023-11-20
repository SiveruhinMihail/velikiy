import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do = False

    def paintEvent(self, event):
        if self.do:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do = False

    def paint(self):
        self.do = True
        self.update()

    def draw_flag(self, qp):
        x, y, z = random.randint(0, 400), random.randint(0, 300), random.randint(0, 400)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, z, z)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
