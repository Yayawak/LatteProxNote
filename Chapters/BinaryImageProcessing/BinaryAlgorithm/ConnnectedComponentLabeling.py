import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import (QLabel, QDial, QWidget, QSlider,
    QVBoxLayout, QHBoxLayout, QPushButton, QDial, QSlider,
    QTextEdit, QLineEdit
    )
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import networkx as nx
# import matplotlib as mpl
from Helpers.QWidgetCanva import QWidgetCanva
import time
from PyQt5.QtCore import QTimer, QPropertyAnimation, QRect, QPoint


# class ConnectedComponentLabeling(QWidget):
class ConnectedComponentLabeling(QWidgetCanva):
    def _debug(self):
        size = (6, 6)
        # size = (10, 10)
        # np.random.seed(0)
        # self.img = np.random.randint(0, 2, size=size)
        self.img = np.random.choice([0, 1], size=size)
        self.labelImg = np.zeros_like(self.img)
        print(self.img)

        # self.equivalentTable = set()
        self.equivalentTable = []

        # plt.imshow(self.img, cmap='gray')
        # print(self.labelImg)
        # print("is [-1,2] out of bound : ",  self.checkIsOutOfBound(-1, 2))
        print()
        self.labelPixel()
        print(self.labelImg)
        print("equiv table")
        # self.equivalentTable = list(set(self.equivalentTable))
        # self.equivalentSet = set(map(frozenset, self.equivalentTable))
        print(self.equivalentTable)
        print()

        print("equiv set")
        # print(self.equivalentSet)
        print()

        print("eqv set !")
        print(self.getEquivalentSet())

        print("relabeling")
        self.relabel()
        print(self.labelImg)

        fig, axs = plt.subplots(ncols=2, figsize=[8, 8])
        axs[0].imshow(self.img, cmap='gray')
        axs[1].imshow(self.labelImg, cmap='inferno')
        # print()
        plt.show()

    def __init__(self):
        super().__init__(2)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # size = (6, 6)
        # # size = (10, 10)
        # # size = (100, 100)
        # # np.random.seed(0)
        # self.img = np.random.choice([0, 1], size=size)
        # # self.img = np.random.uniform(5, 1, size=size) > 4
        # self.labelImg = np.zeros_like(self.img)
        # self.equivalentTable = []

        layout.addWidget(self.canva)

        self.start_anim_btn = QPushButton("Start Animation")
        self.start_anim_btn.clicked.connect(self._start_animation)
        layout.addWidget(self.start_anim_btn)

        self.x_size_line_edit = QLineEdit()
        self.y_size_line_edit = QLineEdit()
        self.img_size_group_layout = QHBoxLayout()
        self.img_size_group_layout.addWidget(self.x_size_line_edit)
        self.img_size_group_layout.addWidget(self.y_size_line_edit)

        layout.addLayout(self.img_size_group_layout)
        # self.dummy_btn = QPushButton("Dummy")
        # self.dummy_btn.clicked.connect(self._update_label_img)
        # layout.addWidget(self.dummy_btn)

    def _start_animation(self):
        size = (
            int(self.x_size_line_edit.text()),
            int(self.y_size_line_edit.text())
        )
        # size = (6, 6)
        self.img = np.random.choice([0, 1], size=size)
        # self.img = np.random.uniform(5, 1, size=size) > 4
        self.labelImg = np.zeros_like(self.img)
        self.equivalentTable = []

        self.canva.axs[0].imshow(self.img, cmap='gray')
        self.canva.axs[1].imshow(self.labelImg, cmap='rainbow')
        # self.labelImg = np.random.normal(5, 3, size=self.labelImg.shape)
        # self._update_label_img()
        # animaiton = QPropertyAnimation(self.canva, b"pos")
        self.labelPixel()
        self.relabel()

    def re_draw_label_img(self):
        # timer = QTimer()
        # timer.timeout.connect(self._update_label_img)
        # timer.start(20)
        # time.sleep(100 / 1000)
        # time.sleep(20 / 1000)
        # time.sleep(40 / 1000)
        self._update_label_img()

    def _update_label_img(self):
        print(self.labelImg)
        # self.canva.axs[0].imshow(self.img, cmap='gray')
        self.canva.axs[1].clear()
        self.canva.axs[1].imshow(self.labelImg, cmap='viridis')
        self.canva.draw()
        # self.canva.pos.

        # self.canva.axs[1].cla()

    def getEquivalentSet(self):
        G = nx.Graph()

        equivalent_list = [list(subset) for subset in self.equivalentTable]
        for subset in equivalent_list:
            G.add_edge(subset[0], subset[1])
        connected_component = nx.connected_components(G)
        output_list = [list(component) for component in connected_component]
        return output_list
        # pos = nx.spring_layout(G)
        # nx.draw(G, pos, with_labels=True)
        # plt.show()

    def relabel(self):
        equivalent_set = self.getEquivalentSet()
        for i in range(self.labelImg.shape[0]):
            for j in range(self.labelImg.shape[1]):
                color = self.labelImg[i, j]
                if color != 0:
                    for sub_list in equivalent_set:
                        if set([color]).issubset(set(sub_list)):
                            self.labelImg[i, j] = min(sub_list)
                            self.re_draw_label_img()

    def labelPixel(self):
        label: int = 0
        leftLabeled: bool = False
        topLabeled: bool = False

        for i in range(self.img.shape[0]):
            for j in range(self.img.shape[1]):
                if (self.img[i, j] == 1):
                    leftLabeled = self.labelImg[i - 1, j] != 0
                    topLabeled = self.labelImg[i, j - 1] != 0
                    # ? Some of left, top already have label
                    if (topLabeled):
                        self.labelImg[i, j] = self.labelImg[i, j - 1]
                        self.re_draw_label_img()

                    elif (leftLabeled):
                        self.labelImg[i, j] = self.labelImg[i - 1, j]
                        self.re_draw_label_img()
                    if (leftLabeled and topLabeled):
                        # ? Both have the same label
                        if (self.labelImg[i - 1, j]
                                == self.labelImg[i, j - 1]):
                            self.labelImg[i, j] = self.labelImg[i - 1, j]
                        # ? Both have diff label
                        else:
                            self.labelImg[i, j] = self.labelImg[i, j - 1]
                            self.equivalentTable.append([
                                self.labelImg[i - 1, j],
                                self.labelImg[i, j - 1],
                            ])
                        self.re_draw_label_img()
                    # ? no left, no right both
                    if (not leftLabeled and not topLabeled):
                        label += 1
                        self.labelImg[i, j] = label
                        self.re_draw_label_img()
                        self.equivalentTable.append([
                            self.labelImg[i, j],
                            self.labelImg[i, j],
                        ])

    def isOutOfBound(self, x, y):
        if (y < 0 or y > len(self.img) - 1):
            return True
        if (x < 0 or x > len(self.img[0] - 1)):
            return True
        return False


# class CCCanva(FigureCanvasQTAgg):
#     def __init__(self):
#         fig = plt.figure()
#         super().__init__(fig)
#         self.ax1 = fig.add_subplot(1, 2, 1)
#         self.ax2 = fig.add_subplot(1, 2, 2)
