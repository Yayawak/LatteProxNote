from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMenuBar \
    , QGridLayout, QPlainTextEdit, QVBoxLayout
# from PyQt5.QtCore import *
from LessonTree import LessonTreeWidget
from DisplayWidget import DisplayWidget

class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.lessonTreeWidget = LessonTreeWidget()
        self.lessonTreeWidget.itemSelectionChanged.\
            connect(self._updateDisplayWidget)
        self.displayWidget = DisplayWidget()

        layout.addWidget(self.lessonTreeWidget, 3)
        layout.addWidget(self.displayWidget, 7)

    def _updateDisplayWidget(self):
        selectedItem = self.lessonTreeWidget.currentItem()
        # selectedItem.
        # if selectedItem is not None:
        if selectedItem is not None and selectedItem.childCount() == 0:
            # self.displayWidget.lb.text = selectedItem
            self.displayWidget.updateContent(str(selectedItem))
            print(selectedItem)
        # else:
            #
            # self.displayWidget.update


