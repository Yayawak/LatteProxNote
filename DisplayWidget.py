from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, \
    QTextEdit
from Chapters.Introduction.IntroductionWidget import IntroductionWidget

class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        # self.lb = QLabel("label")
        # te = QTextEdit("edit me")
        # layout.addWidget(self.lb)
        # layout.addWidget(te)
        intro = IntroductionWidget()
        layout.addWidget(intro)


    def updateContent(self, data):
        self.lb.setText(data)


