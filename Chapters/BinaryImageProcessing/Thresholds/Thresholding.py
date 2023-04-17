from PyQt5.QtWidgets import QLabel, QDial, QWidget, QSlider, \
    QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
import numpy as np
import cv2
# from cv2.
import os
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import Qt


class ThresholdDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.thresholdSlider = QSlider(Qt.Horizontal)
        self.thresholdSlider.setRange(0, 255)
        self.thresholdSlider.setSingleStep(1)
        self.thresholdSlider.setValue(50)
        self.tshLabel = QLabel()

        self.canvas = ThresholdCanvas()
        self.thresholdSlider.valueChanged.connect(self.on_slider_change)
        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.thresholdSlider)
        slider_layout.addWidget(self.tshLabel)
        layout.addLayout(slider_layout)
        layout.addWidget(self.canvas)

    def on_slider_change(self):
        val = self.thresholdSlider.value()
        self.canvas.plot(val)
        self.tshLabel.setText(str(val))


class ThresholdCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = plt.figure()
        super().__init__(fig)
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        fullPath = os.path.join(scriptDir, "cloud strife.webp")
        self.bgr_image = cv2.imread(fullPath)
        self.gray_image = cv2.cvtColor(self.bgr_image, cv2.COLOR_BGR2GRAY)
        self.ax1.imshow(self.bgr_image[:, :, ::-1])
        self.ax2.imshow(self.gray_image, cmap='gray')

    def plot(self, threshold_value):
        ...
        bin_img = np.array(self.gray_image > threshold_value, dtype=int)

        self.ax2.imshow(bin_img, cmap='gray')
        self.draw()
        self.ax2.cla()
