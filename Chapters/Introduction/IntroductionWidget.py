from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, \
    QFileDialog, QTabWidget, QTabBar, QLabel
from Chapters.Introduction.ImageProjectionCanvas import ImageProjectionCanvas
from Chapters.Introduction.ListOfLearn.TopicsList import TopicsListWidget

class IntroductionWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        lb = QLabel("""Introduction widget
                    Mapping Real Coordinate to Image Plane
                    """)
        layout.addWidget(lb)

        layout.addWidget(QLabel("ROADMAP"))
        layout.addWidget(TopicsListWidget())



        # todo : jump between sub sections (making outlier)
        # canvas = ImageProjectionCanvas()

        # layout.addWidget(canvas)
