from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, \
    QFileDialog, QTabWidget, QTabBar, QLabel
from Chapters.Introduction.ImageProjectionCanvas import ImageProjectionCanvas

class IntroductionWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        lb = QLabel("""Introduction widget
                    Mapping Real Coordinate to Image Plane
                    """)
        layout.addWidget(lb)

        canvas = ImageProjectionCanvas()

        layout.addWidget(canvas)
