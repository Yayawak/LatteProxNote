from PyQt5 import QtWidgets
import sys

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        hitBtn = QtWidgets.QPushButton("click me", self)
        self.setGeometry(200, 100, 500, 300)
        self.show()
app = QtWidgets.QApplication(sys.argv)

widget = Widget()

app.exec_()
