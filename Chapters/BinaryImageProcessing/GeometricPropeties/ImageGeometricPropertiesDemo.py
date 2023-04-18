import cv2
import numpy as np
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QLabel, QWidget, QSlider,
                             QVBoxLayout, QHBoxLayout,
                             QCheckBox, QSizePolicy, QPushButton,
                             QRadioButton, QDial)
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from Chapters.BinaryImageProcessing.GeometricPropeties.OrientationOfSingleObject import ImageOrientation
from Chapters.BinaryImageProcessing.GeometricPropeties.ImageCentroid import ImageCentroiding
from Chapters.BinaryImageProcessing.GeometricPropeties.ImageProjection import ImageProjection


class GeomPropertiesDemoWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.dial = QDial()
        self.dial.setRange(0.1, 100)
        self.dial.setSingleStep(0.1)
        self.dial.setValue(50)
        # self.dial.setMaximumWidth(self.width() * 0.3)
        # self.dial.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.dialLabel = QLabel()

        checkboxs_layout = QVBoxLayout()
        self.is_circle_checkbox = QCheckBox("Circle")
        self.is_triangle_checkbox = QCheckBox("Triangle")
        self.is_triangle_checkbox.setChecked(True)
        checkboxs_layout.addWidget(self.is_circle_checkbox)
        checkboxs_layout.addWidget(self.is_triangle_checkbox)

        self.canvas = self.Canva(self)
        self.showHistRadio = QRadioButton("show histogram")

        input_control_layout = QHBoxLayout()
        input_control_layout.addWidget(self.dial)
        input_control_layout.addWidget(self.dialLabel)
        input_control_layout.addLayout(checkboxs_layout)
        input_control_layout.addWidget(self.showHistRadio)
        layout.addLayout(input_control_layout)
        # canva_and_checkbox_layout = QHBoxLayout()
        # canva_and_checkbox_layout.addWidget(self.canvas, 3)
        # canva_and_checkbox_layout.addLayout(checkboxs_layout, 1)
        # self.showHistButton = QPushButton("show histogram")
        # layout.addLayout(canva_and_checkbox_layout, 8)
        layout.addWidget(self.canvas)

        self.dial.valueChanged.connect(self.on_input_change)
        self.showHistRadio.toggled.connect(self.on_input_change)

    def on_input_change(self):
        val = self.dial.value() / 100
        self.canvas.plot(val,
                         self.is_triangle_checkbox.isChecked(),
                         self.is_circle_checkbox.isChecked())
        self.dialLabel.setText(str(val))
        # if not self.is_triangle_checkbox.isChecked():
        #     self.ax1.cla()
        #     self.ax2.cla()


    class Canva(FigureCanvasQTAgg):
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance
            self.fig = plt.figure()
            super().__init__(self.fig)
            self.ax = self.fig.add_subplot(221)
            self.ax1 = self.fig.add_subplot(222, sharey=self.ax)
            self.ax2 = self.fig.add_subplot(223, sharex=self.ax)
            self.ax1.set_visible(False)
            self.ax2.set_visible(False)

            self.image = self.random_shape(True, False)
            self.ax.imshow(self.image, cmap='binary')
            # plt.show()

        def random_shape(self, isTriangle, isCircle):
            size = 50
            # x, y = np.mgrid[0:size, 0:size]
            # distance = np.sqrt((x - size/2)**2 + (y - size/2)**2)
            #
            # inner_ring = (distance >= size / 4) & (distance <= size/3)
            # outer_ring = (distance >= 2*size/5) & (distance <= 3*size/5)
            # donut = inner_ring | outer_ring
            #
            # noise = np.random.normal(loc=.0, scale=1.0, size=(size, size))
            # bend = np.sin(x/size*np.pi*2) * np.cos(y/size*np.pi*2)
            # image = donut.astype(int) + noise*.1 + bend*.1

            image = np.zeros((size, size), dtype=np.uint8)
            #
            # image = cv2.rectangle(image,
            #                       np.random.randint(0, size, size=2),
            #                       np.random.randint(0, size, size=2),
            #                       1, thickness=-1)
            # image *= \
            #     np.array(
            #         np.random.randint(0, 100, size=(size, size), dtype=np.uint8) / 100
            #         , dtype=np.uint8)
            # image *= np.array(np.random.normal(0, size, size=(size, size)), dtype=np.uint8)

            # triangle
            if isTriangle:
                image = cv2.drawContours(image,
                                         [(np.random.rand(3, 2) * size).astype(int)],
                                         0, 1, -1
                                         )
            if isCircle:
                center = np.random.rand(2) * size
                radius = np.random.randint(1, int(size * 0.8))

                # circle
                image = cv2.circle(image, tuple(center.astype(int)),
                                   radius, 1, -1)
            # kernel = np.ones((5, 5), dtype=np.uint8)
            # print("shape of image ", image.shape)
            # image = cv2.erode(image, kernel)
            # image = cv2.dilate(image, kernel)

            return image

        def plot(self, threshold_value, isTriangle, isCircle):
            ...
            # self.ax = self.fig.add_subplot(111)
            bin_image = self.image = self.random_shape(isTriangle, isCircle)
            orientator = ImageOrientation()
            orientator.calculate_moments(bin_image)
            try:
                # self.image = cv2.line(self.image,
                #                       (int(orientator.x_bar), int(orientator.y_bar)),
                #                       (orientator.x_endline, orientator.y_endline),
                #                       (0, 255, 0), thickness=1
                #                       )
                self.ax.plot([orientator.x_bar, orientator.x_endline],
                             [orientator.y_bar, orientator.y_endline],
                             color='green',
                             linewidth=2)
            except Exception:
                pass
            self.ax.imshow(self.image, cmap='binary')
            # plt.plot
            # self.ax.plot()
            cx, cy = ImageCentroiding.find_centroid(self.image)
            print(f"cx,cy = ({cx},{cy})")
            self.ax.scatter([cx], [cy])

            if self.outer_instance.showHistRadio.isChecked():
                # self.ax.cla()
                # self.fig.clf()
                # fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
                # self.fig = fig
                # print("len of axs = ", len(axs))
                # self.ax = self.fig.add_subplot(221)
                # self.ax = axs[0][0]
                self.ax.imshow(self.image, cmap='binary')
                # ax1 = axs[0][1]
                # ax2 = axs[1][0]
                ImageProjection.static_bin_image = self.image
                v = ImageProjection.projectionV()
                h = ImageProjection.projectionH()
                self.ax1.barh(np.arange(len(h)), h)
                self.ax2.bar(np.arange(len(v)), v)
                self.draw()
                self.ax.cla()
                self.ax1.cla()
                self.ax2.cla()
                self.ax1.set_visible(True)
                self.ax2.set_visible(True)
                # self.fig.clf()
            else:
                self.draw()
                self.ax.cla()
                self.ax1.set_visible(False)
                self.ax2.set_visible(False)

