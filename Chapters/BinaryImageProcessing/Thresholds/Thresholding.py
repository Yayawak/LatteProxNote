from PyQt5.QtWidgets import QLabel, QDial, QWidget, QSlider, \
    QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
import numpy as np
import cv2
# from cv2 import cv2
import os
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import Qt

class ThresholdDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        # self.thresholdDial = QDial()
        # self.thresholdDial.setMinimum(0)
        # self.thresholdDial.setMaximum(255)
        self.thresholdSlider = QSlider(Qt.Horizontal)
        self.thresholdSlider.setMinimum(0)
        self.thresholdSlider.setMaximum(255)
        self.tshLabel = QLabel()

        self.canvas = ThresholdCanvas()
        # self.thresholdDial.valueChanged.connect(lambda: self.canvas.plot(self.thresholdDial.value()))
        self.thresholdSlider.valueChanged.connect(self.onSliderChange)
        sliderLayout = QHBoxLayout()
        sliderLayout.addWidget(self.thresholdSlider)
        sliderLayout.addWidget(self.tshLabel)
        layout.addLayout(sliderLayout)
        layout.addWidget(self.canvas)

    def onSliderChange(self):
        val = self.thresholdSlider.value()
        self.canvas.plot(val)
        self.tshLabel.setText(str(val))

class ThresholdCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = plt.figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        fullPath = os.path.join(scriptDir, "cloud strife.webp")
        self.originImg = cv2.imread(fullPath, cv2.IMREAD_GRAYSCALE)
        self.ax.imshow(self.originImg, cmap='gray')
    def plot(self, threshold_value):
        ...
        # bin_img = self.originImg > threshold_value
        bin_img = np.array(self.originImg > threshold_value, dtype=int)
        print(bin_img)
        self.ax.imshow(bin_img, cmap='gray')
        self.draw()
        self.ax.cla()
        # self.draw()

    # def getImage(self):
    #     pxmap = QPixmap(fullPath)
    #     return pxmap.scaled(self.width(),
    #                         self.height(),
    #                         aspectRatioMode=QtCore.Qt.KeepAspectRatio,
    #                         transformMode=QtCore.Qt.SmoothTransformation
    #                         )
