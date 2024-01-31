from PyQt5.QtWidgets import QWidget, QTreeWidget, QVBoxLayout, \
    QTreeWidgetItem
from Ini.IndexTree.TreeWidgetChapter import TreeWidgetChapter
from Chapters.Introduction.IntroductionWidget import IntroductionWidget
from Chapters.Introduction.ImageProjectionCanvas import ImageProjectionCanvas
from Chapters.Introduction.SampleQuantation.SampQuant import SampQuant
from Chapters.Introduction.ImageConstructionProgram.ImageConstructCanvas import ImageConstructCanvas
from Chapters.BinaryImageProcessing.Thresholds.Thresholding import ThresholdDemo
from Chapters.BinaryImageProcessing.BinImgMainWidget import BinImgMainWidget
from Calculus.SequenceSeries.IntroductionToSeqSer import IntroductionToSeqSer
from Chapters.BinaryImageProcessing.BinaryAlgorithm.ConnnectedComponentLabeling import ConnectedComponentLabeling

class LessonTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(['Chapter', 'section'])
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 50)

        # todo : plan layout of this book store it in data collector mvc 'M'
        # * ----- chapter 0 : no really image processing but calculus  -------------------------
        TreeWidgetChapter(self, "sequence and series", IntroductionToSeqSer())



        # * -------------------------- chapter 1  -------------------------
        introductionItem = TreeWidgetChapter(
            self, "introduction", IntroductionWidget())
        TreeWidgetChapter(introductionItem, "mapping real world to image plane", ImageProjectionCanvas())
        TreeWidgetChapter(introductionItem, "sampling and quantization", SampQuant())
        TreeWidgetChapter(introductionItem, "camera plane and projection to image plane homework", ImageConstructCanvas())

        # * -------------------------- chapter 2  -------------------------
        binaryImageProcessing = TreeWidgetChapter(
            self, "binary image processing", BinImgMainWidget()
        )
        TreeWidgetChapter(binaryImageProcessing, "Thresholding", ThresholdDemo())
        geometricProperties = TreeWidgetChapter(binaryImageProcessing, "Geometric Properties")
        TreeWidgetChapter(binaryImageProcessing, "Projections")
        TreeWidgetChapter(binaryImageProcessing, "Run-lenght Encoding")
        binaryAlgotithms = TreeWidgetChapter(binaryImageProcessing, "Binary Algorithm")
        TreeWidgetChapter(binaryAlgotithms, "component labeling", ConnectedComponentLabeling())
        TreeWidgetChapter(binaryAlgotithms, "size filter")
        TreeWidgetChapter(binaryAlgotithms, "euler number")
        TreeWidgetChapter(binaryAlgotithms, "region boundary")
        TreeWidgetChapter(binaryAlgotithms, "area and perimeter")
        TreeWidgetChapter(binaryAlgotithms, "compactness")
        TreeWidgetChapter(binaryAlgotithms, "distance measures")
        TreeWidgetChapter(binaryAlgotithms, "distancc transform")
        TreeWidgetChapter(binaryAlgotithms, "medial axis")
        TreeWidgetChapter(binaryAlgotithms, "thinning")
        TreeWidgetChapter(binaryAlgotithms, "expanding and shrinking")

        TreeWidgetChapter(binaryImageProcessing, "Morphological Operations")
        TreeWidgetChapter(binaryImageProcessing, "Optical Character recognition")
        TreeWidgetChapter(binaryImageProcessing, "homework")
        # * -------------------------- chapter 3  -------------------------
        regions = TreeWidgetChapter(
            self, "regions"
        )
        # * -------------------------- chapter 4  -------------------------
        imageFiltering = TreeWidgetChapter(
            self, "image filtering"
        )
        # * -------------------------- chapter 5  -------------------------
        edgeDetection = TreeWidgetChapter(
            self, "edge detection"
        )
        # * -------------------------- chapter 6  -------------------------
        contour = TreeWidgetChapter(
            self, "contour"
        )
        # * -------------------------- chapter 7  -------------------------
        texture = TreeWidgetChapter(
            self, "texture"
        )
        # * -------------------------- chapter 8  -------------------------
        optics = TreeWidgetChapter(
            self, "optics"
        )
        # * -------------------------- chapter 9  -------------------------
        shading = TreeWidgetChapter(
            self, "shading"
        )
        # * -------------------------- chapter 10  -------------------------
        color = TreeWidgetChapter(
            self, "color"
        )
        # * -------------------------- chapter 11  -------------------------
        depth = TreeWidgetChapter(
            self, "depth"
        )
        # * -------------------------- chapter 12  -------------------------
        callibration = TreeWidgetChapter(
            self, "callibration"
        )
        # * -------------------------- chapter 13  -------------------------
        curveAndSurface = TreeWidgetChapter(
            self, "curve & surface"
        )
        # * -------------------------- chapter 14  -------------------------
        dynamicVision = TreeWidgetChapter(
            self, "dynamic vision"
        )
        # * -------------------------- chapter 15  -------------------------
        objectRecongition = TreeWidgetChapter(
            self, "object recognition"
        )


