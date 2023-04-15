from PyQt5.QtWidgets import QTreeWidgetItem, QWidget

class TreeWidgetChapter(QTreeWidgetItem):
    def __init__(self, parent, name, widget=None):
        super().__init__(parent, [name])
        if widget:
            self.widget = widget
        else:
            self.widget = QWidget()
