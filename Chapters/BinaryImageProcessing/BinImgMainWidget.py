from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QTabWidget, QAction
                             )
from Chapters.BinaryImageProcessing.Thresholds.Thresholding import ThresholdDemo
from Chapters.BinaryImageProcessing.GeometricPropeties.ImageGeometricPropertiesDemo import GeomPropertiesDemoWidget
from PyQt5.QtCore import pyqtSlot

class BinImgMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.threshold_demo_widget = ThresholdDemo()
        self.centre_of_mass_widget = GeomPropertiesDemoWidget()
        # main_layout.addWidget(threshold_demo_widget)
        # main_layout.addWidget(centre_of_mass_widget)
        # self._main_display_widget = QWidget()

        self.tabs.addTab(self.threshold_demo_widget, "Thresholding")
        self.tabs.addTab(self.centre_of_mass_widget, "Geometric properties")
        self.main_layout.addWidget(self.tabs)
        # self.main_layout.addWidget(self.main_display_widget)

        # self.tabs.currentChanged.connect(lambda : self.on_tab_change())
        self.tabs.currentChanged.connect(self.on_tab_change)
        self.setLayout(self.main_layout)

    def on_tab_change(self, idx):
        currentIdx = self.tabs.currentIndex()
        print("tab changed")
        print("current one is ", currentIdx)
        # self.main_display_widget = currentIdx

    # @property
    # def main_display_widget(self):
    #     return self._main_display_widget
    #
    # @main_display_widget.setter
    # def main_display_widget(self, w):
    #     self._main_display_widget = w
