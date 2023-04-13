from PyQt5.QtWidgets import QMenuBar, QHBoxLayout, QMenu

class LessonMenuBar(QMenuBar):
    def __init__(self, parent):
        # super(LessonMenuBar, self).__init__(parent)
        # super(LessonMeniuBar, self).__init__(parent)
        super().__init__(parent)
        # layout = QHBoxLayout()

        # introductionMenu = QMenu("&Introduction", parent)
        # introductionMenu = QMenu("Introduction", self)

        # introductionMenu = self.addMenu("Lesson")
        # c2 = self.addMenu("C2")
        self.addMenu("File")
        self.addMenu("Edit")
        print("Hello menu bar inited")
        # introductionMenu = addMenu(introductionMenu)
        # introductionMenu.addAction("Machine Vision")

        # self.setLayout(layout)
