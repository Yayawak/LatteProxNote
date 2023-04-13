from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, \
    QTextEdit
from Chapters.Introduction.IntroductionWidget import IntroductionWidget

class DisplayWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.lb = QLabel("This is display widget")
        # te = QTextEdit("edit me")
        self.layout.addWidget(self.lb)
        # layout.addWidget(te)
        # self.updateCurrentWidget(Intr)
        # intro = IntroductionWidget()
        # layout.addWidget(intro)



    def updateCurrentWidget(self, widget):
        # self.layout.remove(self.layout)
        # ! potential be bug
        # for child in self.layout.children():
        #     self.layout.removeWidget(child)
        # for i in reversed(range(self.layout.count())):
        #     self.layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()

        self.layout.addWidget(widget)



