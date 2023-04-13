from PyQt5.QtWidgets import QWidget, QTreeWidget, QVBoxLayout, \
    QTreeWidgetItem
from Chapters.Introduction.IntroductionWidget import IntroductionWidget
from Chapters.Introduction.ImageProjectionCanvas import ImageProjectionCanvas

class LessonTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(['Chapter', 'Page'])
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 50)
        # for i in range(1, 6):
        #     chapterItem = QTreeWidgetItem(self,
        #         ['Chapter ' + str(i) + ''])
        #     for j in range(1, 6):
        #         # pageItem = QTreeWidgetItem(chapterItem, ['Page ' + str(j) + ''])
        #         section = TreeWidgetChapter(chapterItem)

        # todo : plan layout of this book store it in data collector mvc 'M'
        introductionItem = TreeWidgetChapter(
            self, "introduction", IntroductionWidget())
        TreeWidgetChapter(introductionItem, "mapping real world to image plane", ImageProjectionCanvas())

class TreeWidgetChapter(QTreeWidgetItem):
    def __init__(self, parent, name, widget):
        super().__init__(parent, [name])
        self.widget = widget
