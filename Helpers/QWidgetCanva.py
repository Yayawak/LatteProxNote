from PyQt5.QtWidgets import QLabel, QDial, QWidget, QSlider, \
    QVBoxLayout, QHBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib import pyplot as plt
# import numpy as np


class QWidgetCanva(QWidget):
    # def __init__(self, axs_size: np.array):
    # ? n_axs = 3 -> 3 cols 1 row
    def __init__(self, n_axs: int):
        super().__init__()
        self.canva = Canva(n_axs)


class Canva(FigureCanvasQTAgg):

    def __init__(self, n_axs: int):
        self.fig = plt.figure()
        super().__init__(self.fig)
        self.axs = []
        # self.axs = [self.fig.add_subplot('11' + str(i + 1)) for i in range(n_axs)]
        # self.axs = [self.fig.add_subplot(
        #     '1' + str(n_axs) + str(i + 1)) for i in range(n_axs)]
        # self.axs = [self.fig.add_subplot(
        #     '12' + str(i + 1)) for i in range(n_axs)
        # ]
        for i in range(n_axs):
            self.axs.append(
                self.fig.add_subplot(
                    int(str(
                        '1'
                        + str(n_axs)
                        + str(i + 1)
                    ))
                )
            )
        # self.axs.append(self.fig.add_subplot(int('121')))
        # self.axs.append(self.fig.add_subplot(int('122')))
        # self.ax1 = fig.add_subplot(121)
        # self.ax2 = fig.add_subplot(122)
        # self.fig.add_subplots()
        # self.fig.
        # plt.figure()
        # plt.ax
