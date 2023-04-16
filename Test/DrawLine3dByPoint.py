import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, \
    QVBoxLayout, QHBoxLayout, QDial, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

def override(func):
    """A decorator to indicate that a method overrides a method in a superclass."""
    return func

class TreeDLinePlotWidget(QWidget):
    class Canvas(FigureCanvasQTAgg):
        def __init__(self):
            fig = plt.figure()
            super().__init__(fig)
            self.ax = fig.add_subplot(111, projection='3d')

    def __init__(self):
        super().__init__()
        self.p1Lb = QLabel("Point 1:")
        self.p2Lb = QLabel("Point 2:")

        self.cv = self.Canvas()

        inputLayout = QVBoxLayout()

        self.dialsP1P2 = [[QDial() for _ in range(3)] for œ in range(2)]
        self.dialTwoPointsLayout = [QHBoxLayout() for _ in range(2)]
        self.dialTwoPointsLayout[0].addWidget(self.p1Lb)
        self.dialTwoPointsLayout[1].addWidget(self.p2Lb)
        self.pointIndicatorLabels = [QLabel() for i in range(2)]
        for i, dialArrP_i in enumerate(self.dialsP1P2):
            for d in dialArrP_i:
                self.dialTwoPointsLayout[i].addWidget(d)
                d.valueChanged.connect(self.plot)
            inputLayout.addLayout(self.dialTwoPointsLayout[i])
            self.dialTwoPointsLayout[i].addWidget(self.pointIndicatorLabels[i])

        buttonLayout = QHBoxLayout()

        mainlayout = QVBoxLayout()
        mainlayout.addLayout(inputLayout)
        mainlayout.addLayout(buttonLayout)



        self.setLayout(mainlayout)

        mainlayout.addWidget(self.cv)


    @override
    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 3)
        painter.setPen(pen)
        painter.drawLine(
            0, self.height() / 2,
            self.width(), self.height() / 2
        )

    def plot(self):
        lays = [self.dialTwoPointsLayout[i] for i in range(2)]
        p1 = [lays[0].itemAt(i).widget().value() for i in range(1, 4)]
        p2 = [lays[1].itemAt(i).widget().value() for i in range(1, 4)]
        pos12 = x, y, z = [*[
            [int(p[i]) for p in [p1, p2]] for i in range(3)
        ]]
        print(f"x,y,z = ({x},{y},{z})")
        self.cv.ax.set_xlim(0, 100)
        self.cv.ax.set_ylim(0, 100)
        self.cv.ax.set_zlim(0, 100)
        self.cv.ax.plot(x, y, z)
        for i in range(2):
            self.pointIndicatorLabels[i].setText(f"{x[i]},{y[i]},{z[i]}")
        self.cv.draw()
        self.cv.ax.cla()
