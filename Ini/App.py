from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from Ini.MainWidget import MainWidget
# from Helpers.GridPainter import GridPainter
# from SideProjects.DigitRecongnition.DigitRegDemo import DigitRegDemo
# from Calculus.SequenceSeries.IntroductionToSeqSer import IntroductionToSeqSer


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Image Processing Notebook by Yawak"
        self.setGeometry(200, 20, 1000, 700)
        self.setWindowTitle(self.title)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        # import PyQt5
        # print(PyQt5.__file__)

        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)

        # self.setCentralWidget(IntroductionToSeqSer())
        # self.setCentralWidget(BinaryAlgorithmsDemo())
        # self.setCentralWidget(GridPainter(100, 100))
        # self.setCentralWidget(GridPainter(20,20))
        # self.setCentralWidget(DigitRegDemo())
        self.show()
