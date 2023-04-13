from PyQt5.QtWidgets import QWidget, QTreeWidget, QVBoxLayout, \
    QTreeWidgetItem

# class LessonTreeWidget(QWidget):
#     def __init__(self, parent=None):
#         super(LessonTreeWidget, self).__init__(parent)
#         self.tree = QTreeWidget()
#         self.tree.setHeaderLabels(['Chapter', 'Page'])
#         self.tree.setColumnWidth(0, 200)
#         self.tree.setColumnWidth(2, 50)

#         layout = QVBoxLayout()
#         layout.addWidget(self.tree)
#         self.setLayout(layout)

    # def add_chapter(self, chapterName, pages):
    #     chapterItem = QTreeWidgetItem(self.tree, [chapterName])
    #     for page in pages:
    #         pageItem = QTreeWidgetItem((chapterItem, [page]))

class LessonTreeWidget(QTreeWidget):
    # def __init__(self, parent):
    def __init__(self):
        super().__init__()
        # super(LessonTreeWidget, self).__init__(parent)
        self.setHeaderLabels(['Chapter', 'Page'])
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 50)
        for i in range(1, 6):
            chapterItem = QTreeWidgetItem(self,
                ['Chapter ' + str(i) + ''])
            for j in range(1, 6):
                pageItem = QTreeWidgetItem(chapterItem, ['Page ' + str(j) + ''])

