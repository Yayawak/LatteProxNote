from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout
    , QPushButton, QSlider, QFileDialog
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtGui import QPixmap
from PyQt5.Qt import Qt
from PyQt5 import QtCore
import os
import numpy as np
from Helpers.Utils import pixMapToArray, imgArrToPixmap, rgbaToGray
import matplotlib.pyplot as plt

class SampQuant(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.imgLb = QLabel()
        self.downSampBtn = QPushButton("down sample")
        layout.addWidget(self.downSampBtn)

        self.w, self.h = self.imgLb.width(), self.imgLb.height()
        scaledImage = self.getImage()
        self.imgLb.setPixmap(scaledImage)

        # todo : numpy array sampling
        self.originArr = pixMapToArray(scaledImage)
        # print(self.originArr)

        self.downSampBtn.clicked.connect(self._updateLabelImage)

        freqSlider = QSlider(Qt.Horizontal)
        freqSlider.setMinimum(1)
        freqSlider.setMaximum(100)
        layout.addWidget(freqSlider)

        freqSlider.valueChanged.connect(lambda: self._updateLabelImage(
            f"{str(freqSlider.value())}x{str(freqSlider.value())}"
        ))

        hLayout = QHBoxLayout()
        layout.addLayout(hLayout)
        hLayout.addWidget(self.imgLb)

        class HistCanvas(FigureCanvasQTAgg):
            def __init__(self, originArr):
                fig = Figure()
                super().__init__(fig)
                ax = fig.add_subplot(111)
                flat = originArr.reshape(-1, 4)
                grays = [rgbaToGray(rgba) for rgba in flat]
                ax.hist(grays, 256, [0, 256])
        hLayout.addWidget(HistCanvas(self.originArr))




    def _updateLabelImage(self, size):
        downImg = self.downSample(self.originArr, size)
        print(size)
        downPix = imgArrToPixmap(downImg)
        downPix = downPix.scaled(
            self.w, self.h,
            aspectRatioMode=QtCore.Qt.KeepAspectRatio,
            transformMode=QtCore.Qt.SmoothTransformation
        )
        # self.downSampBtn.clicked.connect(lambda: self._updateLabelImage(downPix))
        self.imgLb.setPixmap(downPix)

    # def downSample(self, imgArr, f):
    #     # [m, n, c] = imgArr.shape
    #     m, n, c = imgArr.shape
    #     # m = imgArr.shape[0]
    #     # n = imgArr.shape[1]
    #     # c =
    #     print("Image shape :", m, n)
    #     tmp = np.zeros((m // f, n // f, c), dtype=np.int8)
    #     print("tmp shape", tmp.shape)
    #     for i in range(0, m, f):
    #         for j in range(0, n, f):
    #             try:
    #                 # tmp[i // f][j // f] = imgArr[i][j]
    #                 tmp[i // f, j // f, :] = imgArr[i, j, :]
    #                 # tmp[i // f][j // f] = 100
    #                 # print(imgArr[i][j])
    #             except IndexError:
    #                 pass
    #     return tmp

    def downSample(self, imgArr, outputSize):
        # h, w = imgArr.shape[:2]
        m, n, c = imgArr.shape
        print("Original image shape : ", m, n, c)
        sH, sW = map(int, outputSize.split("x"))
        mNew = m // sH
        nNew = n // sW
        downsampled = np.zeros((mNew, nNew, c), dtype=np.uint8)

        # for k in range(c):
        for i in range(mNew):
            for j in range(nNew):
                downsampled[i, j] = imgArr[i * sH][j * sW]
                # downsampled[i, j, k] = imgArr[i * sH,j * sW, k]
                # rectangle = imgArr[i*m : (i+1)*m,
                                # j*n : (j+1)*n]
                # avgColor = np.mean(np.mean(rectangle, axis=0),
                #                 axis=0).astype(np.uint8)
                # color = np.mean(rectangle, axis=(0, 1))
                # downsampled[i, j] = color
        print("Down sampled image shape : ", mNew, nNew, c)
        # plt.imshow(downsampled, cmap='giway')
        # plt.show()
        return downsampled

    def getImage(self):
        scriptDir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(scriptDir, "Nikifilini.jpg")
        # path, _ = QFileDialog.getOpenFileName(self, "Open image", "Image files (*.png *.jpeg *.jpg)")
        pixmap = QPixmap(path)
        scaledImage = pixmap.scaled(
            self.w, self.h,
            aspectRatioMode=QtCore.Qt.KeepAspectRatio,
            transformMode=QtCore.Qt.SmoothTransformation
        )
        return scaledImage
