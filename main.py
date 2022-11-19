from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
import sys
from random import choice, randint
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.ok = False
        self.colors = [Qt.red, Qt.yellow, Qt.green, Qt.cyan]

    def run(self):
        self.chislo = randint(10, 200)
        self.color = choice(self.colors)
        self.ok = True

    def paintEvent(self, event):
        if self.ok:
            self.qp = QPainter(self)
            self.qp.begin(self)
            self.draw()
            self.qp.end()
            self.update()

    def draw(self):
        self.qp.setPen(QPen(self.color, 8, Qt.SolidLine))
        self.qp.drawEllipse(self.chislo, self.chislo, self.chislo, self.chislo)


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exit(app.exec())
