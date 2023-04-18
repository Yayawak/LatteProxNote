from PyQt5.QtWidgets import (QWidget, QLabel, QDial, QPushButton,
                             QSlider, QHBoxLayout, QVBoxLayout,
                             QCheckBox, QGridLayout, )
from PyQt5.QtGui import (QPixmap)
import numpy as np

class BinaryAlgorithmsDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.cols = 6
        self.rows = 5

        gridBoard = GridBoardWidget(self)
        layout.addWidget(gridBoard)
        self.setLayout(layout)

        # gridBoard.layout.

    def onclick(self):
        ...

class GridBoardWidget(QWidget):
    def __init__(self, binAlgo: BinaryAlgorithmsDemo):
        super().__init__()
        self.bin_algo = binAlgo
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        for i in range(self.bin_algo.rows):
            for j in range(self.bin_algo.cols):
                    # QWidget()
                pos = (i, j)
                name = f"{str(i)},{str(j)}"
                w = QLabel(name)
                w.setStyleSheet("background-color: orange;")
                w.setMouseTracking(True)
                # w.enterEvent.connect(lambda : print("enter %s" % name))
                self.layout.addWidget(w, *pos)

    # class
        # def on_grid_click(self):

