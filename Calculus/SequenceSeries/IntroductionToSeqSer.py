from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
# import numpy as np
# from pydantic import BaseModel
from PyQt5.QtWidgets import (QWidget)
# from typing import TypeVar, Type
# from typing import Type
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
# from PyQt5 import *


class IntroductionToSeqSer(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, ev):
        qp: QPainter = QPainter(self)
        brush = QBrush(Qt.SolidPattern)
        pen = QPen(Qt.black)
        qp.setBrush(brush)
        qp.setPen(pen)
        # qp.drawRect(50, 50, 100, 100)
        # qp.
        # w = self.width
        # h = self.height
        # qp.drawRect(0.1 * w, 0.1 * h, 50, 100)
        # w
        # self.


# T = TypeVar('T', bound=Axes3D)


class SeqSerCanva(FigureCanvasQTAgg):
    # ax: T
    # ax: Type("mpl_toolkits.mplot3d.axes3d.Axes3D")
    # k : int
    # ax: Axes3D

    def __init__(self):
        # self.ax.
        # self.k.
        fig = Figure()
        super().__init__(fig)
        # self.ax = fig.add_subplot(111, projection='3d')
        self.ax: Axes3D = fig.add_subplot(111, projection='3d')
        # self.a.
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
        # self.ax.plot()
        # self.ax.
        # self.ax.
        # self.ax.
        # self.ax.plot()
        # self.ax.
