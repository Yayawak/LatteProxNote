from PyQt5.QtWidgets import (QListWidget, QWidget)

class TopicsListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        topicList = ["binary image",
            "morphology",
            "image region (ROI)",
            "filtering image",
            "enhancing image",
            "edge detection",
            "contouring image",
            "texture",
            "surface inspection",
            "scene classification",
            "surface orientation",
            "shape determination",
            "geometrical optics",
            "radiometry",
            "color",
            "recover depth information from image (passive / active methods)",
            "3 dimensional image",
            "camera calibration",
            "location and orientation of the camera for recovering 3 d information of images",
            "curves in space",
            "surfaces in space",
            "interpolation technique",
            "approximation techinque",
            "dynamic vision (changes in images segment / motion / track objects)",
            "stucture from motion",
            "object recognition",
            "robotic image",
            "visualization",
            "reverse engineering"
            ]
        self.insertItems(0, topicList)
        # for topic in topicList:
            # self.insertItem(0, "A")
