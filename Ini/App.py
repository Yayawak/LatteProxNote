from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QAction, QTabWidget, QVBoxLayout, \
    QMainWindow, QMenu, QMenuBar, QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSlot
from Ini.LessonMenuBar import LessonMenuBar
from Ini.MainWidget import MainWidget

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Processing Notebook by Yawak"
        self.setGeometry(200, 200, 700, 300)
        self.setWindowTitle(self.title)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)


        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)

        self.show()
