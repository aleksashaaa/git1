import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Круги')
        self.btn = QPushButton(self)
        self.btn.setText('DO')
        self.btn.move(300, 370)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.do)
        self.t = False

    def do(self):
        self.t = True
        self.n = random.randint(0, 300)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)

    def paintEvent(self, event):
        if self.t:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(self.r, self.g, self.b))
        qp.drawEllipse(0, 0, self.n, self.n)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())