from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             )
from PyQt5.QtGui import QPixmap, QPainter, QPen, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, pyqtSignal, QObject, pyqtSlot
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# import matplotlib.backends.backend_qt5agg import
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from Helpers.GridPainter import GridPainter
import time
import os
import cv2
import numpy.typing as npt
# from DigitClassifier import  DigitClassifier
from SideProjects.DigitRecongnition.DigitClassifier import DigitClassifier

# import DigitClassifier

class DigitRegDemo(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.setLayout(layout)

        self.submit_btn = QPushButton("create image")
        self.submit_btn.clicked.connect(self.on_submit)
        self.predict_btn = QPushButton("predict image")
        self.predict_btn.clicked.connect(self.on_predict)
        top_layout.addWidget(self.submit_btn)
        top_layout.addWidget(self.predict_btn)

        self.grid_painter = GridPainter(10, 10)
        self.output_widget = QWidget()
        self.predicted_result_lb = QLabel("result of prediction")
        output_layout = QVBoxLayout()
        self.output_widget.setLayout(output_layout)
        output_layout.addWidget(self.predicted_result_lb)

        bot_layer = QHBoxLayout()
        bot_layer.addWidget(self.grid_painter, 8)
        bot_layer.addWidget(self.output_widget, 2)
        layout.addLayout(bot_layer)

        self.digitClassifier = DigitClassifier()
    # class Canva(FigureCanvasQTAgg:)
    #     def __int__(self):
    #         super().__int__()
    def on_predict(self):
        current_grid_img = self.grid_painter.get_image_grid()
        predicted_output = self.digitClassifier.predict_if_that_is_digit_one(current_grid_img)
        self.predicted_result_lb.setText(str(predicted_output))
        self.grid_painter.reset_grid()

    def on_submit(self):
        img = self.grid_painter.get_image_grid()
        name = f"image_{str(time.time())}.jpeg"
        full_path = os.path.join(DigitClassifier.one_path_dir, name)
        print("full path to save image = ", full_path)
        plt.imsave(full_path, img, cmap='gray')
        self.grid_painter.reset_grid()
        print("image saved", img.shape)

