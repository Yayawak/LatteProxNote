from PyQt5.QtWidgets import QWidget, QTreeWidget, QVBoxLayout, \
    QTreeWidgetItem
from Ini.IndexTree.TreeWidgetChapter import TreeWidgetChapter
from Chapters.Introduction.IntroductionWidget import IntroductionWidget
from Chapters.Introduction.ImageProjectionCanvas import ImageProjectionCanvas
from Chapters.Introduction.SampleQuantation.SampQuant import SampQuant
from Chapters.Introduction.ImageConstructionProgram.ImageConstructCanvas import ImageConstructCanvas

class InterestingTree(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(['Chapter', 'section'])
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 50)

        # todo : plan layout of this book store it in data collector mvc 'M'
        TreeWidgetChapter(self, "soft body : coding train")
        TreeWidgetChapter(self, "hilbert curve")
        TreeWidgetChapter(self, "worley noise")
        TreeWidgetChapter(self, "a* pathfinding")
        TreeWidgetChapter(self, "code snake game")
        TreeWidgetChapter(self, "perlin noise")
        TreeWidgetChapter(self, "starfield in processing")
        TreeWidgetChapter(self, "fractal tree")
        TreeWidgetChapter(self, "directional field")
        TreeWidgetChapter(self, "euler method")
        TreeWidgetChapter(self, "wave function collapse")
        TreeWidgetChapter(self, "path following (steering)")
        TreeWidgetChapter(self, "bezier curve")
        TreeWidgetChapter(self, "wander steering behavior")
        TreeWidgetChapter(self, "self avoiding walk")
        TreeWidgetChapter(self, "simple pendulum")
        TreeWidgetChapter(self, "collatz conjecture")
        TreeWidgetChapter(self, "sould classification")
        TreeWidgetChapter(self, "dijkstra")
        TreeWidgetChapter(self, "pulleys")
        TreeWidgetChapter(self, "levers")
        TreeWidgetChapter(self, "gears")
        TreeWidgetChapter(self, "face auto bluring")
        TreeWidgetChapter(self, "web embedded on app : terraria wiki all data but my UI")
        TreeWidgetChapter(self, "genetic algorithm ai generation sticky man")
        TreeWidgetChapter(self, "simulate clothe")
        TreeWidgetChapter(self, "inverse kinematic for game")
        TreeWidgetChapter(self, "forward kinematic for game")



