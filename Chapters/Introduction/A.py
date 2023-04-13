
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
# from mpl_toolkits.mplot3d import axes3d, Axes3D
# from PyQt5.QtCore import Qt, Slot
# import matplotlib.pyplot as plt
import numpy as np

class ImageProjectionCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.fig = Figure(figsize=(8, 6), dpi=100)
        # self.fig = plt.figure()
        # self.axes = fig.add_subplot(111)
        # self.ax = Axes3D(fig)
        self.ax = self.fig.add_subplot(111, projection='3d')
        super(ImageProjectionCanvas, self).__init__(self.fig)
        # # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.updateGeometry()

        p1 = (0, 0, 0)
        p2 = (3, 4, 10)
        x, y, z = zip(p1, p2)
        self.ax.plot(x, y, z)
        # self.ax.set_xlim3d(-max(x), max(x))
        # self.ax.set_ylim3d(-max(y), max(y))
        # self.ax.set_zlim3d(-max(z), max(z))

        # self.ax.set_xlim3d(min(x), max(x))
        # self.ax.set_ylim3d(min(y), max(y))
        # self.ax.set_zlim3d(min(z), max(z))

        # self.ax.set_xlim([-5, 5])
        # self.ax.set_ylim([-5, 5])
        # self.ax.set_zlim([-20, 20])

        lineDir = np.array(p2) - np.array(p1)
        xUnitVec = np.array([1, 0, 0])
        projLen = np.dot(lineDir, xUnitVec)
        xProj = projLen * xUnitVec

        # for p in [p1, p2]:
        #     x, y, z = p
        #     self.ax.plot([x, x,], [y, 0], [z, 0])
        #     self.ax.plot([x, 0,], [y, y], [z, 0])
        #     self.ax.plot([x, 0,], [y, 0], [z, z])
        self.ax.plot([p1[0], p2[0]],
                    [p1[1], p2[1]],
                    [p1[2], p2[2]]
                    , color='green')
        self.ax.plot([0, xProj[0]],
                    [0, xProj[1]],
                    [0, xProj[2]]
                    , color='red')

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
