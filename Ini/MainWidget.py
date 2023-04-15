from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMenuBar \
    , QGridLayout, QPlainTextEdit, QVBoxLayout, QLabel
# from PyQt5.QtCore import *
from Ini.IndexTree.LessonTree import LessonTreeWidget
from Ini.DisplayWidget import DisplayWidget
from Ini.InterestingTopicsTree.InterestingTree import InterestingTree

class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        self.setLayout(layout)

        self.lessonTreeWidget = LessonTreeWidget()
        self.lessonTreeWidget.itemSelectionChanged.\
            connect(self._updateDisplayWidget)
        self.displayWidget = DisplayWidget()

        vLayout = QVBoxLayout()
        layout.addLayout(vLayout, 3)
        vLayout.addWidget(QLabel("Image processing"))
        vLayout.addWidget(self.lessonTreeWidget)
        vLayout.addWidget(QLabel("Interesting topics"))
        vLayout.addWidget(InterestingTree())
        layout.addWidget(self.displayWidget, 7)

    def _updateDisplayWidget(self):
        selectedItem = self.lessonTreeWidget.currentItem()
        # selectedItem.
        # if selectedItem is not None:
        # if selectedItem is not None and selectedItem.childCount() == 0:
        if selectedItem is not None: # ? this is for making BigChapter can lay some  introducion part before dive in real world
            # self.displayWidget.lb.text = selectedItem
            # self.displayWidget.updateContent(str(selectedItem))
            # ! potential bug if selectedItem is not widget
            self.displayWidget.updateCurrentWidget(selectedItem.widget)
            # print(selectedItem)
        # else:
            #
            # self.displayWidget.update


