from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             )
from PyQt5.QtGui import QPixmap, QPainter, QPen, QMouseEvent, QKeyEvent
from PyQt5.QtCore import Qt, pyqtSignal, QObject, pyqtSlot
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from Helpers.GridPainter import GridPainter
import time
import os

class DigitRegDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        layout.addLayout(top_layout)
        self.setLayout(layout)

        self.submit_btn = QPushButton("create image")
        self.submit_btn.clicked.connect(self.on_submit)
        top_layout.addWidget(self.submit_btn)

        self.grid_painter = GridPainter(10, 10)
        layout.addWidget(self.grid_painter)

    def on_submit(self):
        img = self.grid_painter.get_image_grid()
        # img.tofile("img.bin")
        print(img)
        print(img.shape)
        # im = Image.fromarray(img, dtype=np.uint8)
        path_dir = os.path.dirname(os.path.abspath(__file__))
        path_dir = os.path.join(path_dir, "digits/ones")

        name = f"image_{str(time.time())}.jpeg"
        full_path = os.path.join(path_dir, name)
        # matplotlib.image.imsave(name, img)
        print("full path to save image = ", full_path)
        plt.imsave(full_path, img, cmap='gray')
        self.grid_painter.reset_grid()
        # Image.fromarray(img, mode='1').save(name)

        # im.save(name)



