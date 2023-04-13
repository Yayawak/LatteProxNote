from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

# class ImageProjectionCanvas(FigureCanvasQTAgg):
#     def __init__(self):
#         self.fig = Figure(figsize=(8, 6), dpi=100)
#         # self.fig = plt.figure()
#         # self.axes = fig.add_subplot(111)
#         # self.ax = Axes3D(fig)
#         self.ax = self.fig.add_subplot(111, projection='3d')
#         super(ImageProjectionCanvas, self).__init__(self.fig)
#         # # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         # self.updateGeometry()

#         p1 = (0, 0, 0)
#         p2 = (3, 4, 10)
#         x, y, z = zip(p1, p2)
#         self.ax.plot(x, y, z)
#         # self.ax.set_xlim3d(-max(x), max(x))
#         # self.ax.set_ylim3d(-max(y), max(y))
#         # self.ax.set_zlim3d(-max(z), max(z))

#         # self.ax.set_xlim3d(min(x), max(x))
#         # self.ax.set_ylim3d(min(y), max(y))
#         # self.ax.set_zlim3d(min(z), max(z))

#         # self.ax.set_xlim([-5, 5])
#         # self.ax.set_ylim([-5, 5])
#         # self.ax.set_zlim([-20, 20])

#         lineDir = np.array(p2) - np.array(p1)
#         xUnitVec = np.array([1, 0, 0])
#         projLen = np.dot(lineDir, xUnitVec)
#         xProj = projLen * xUnitVec

#         # for p in [p1, p2]:
#         #     x, y, z = p
#         #     self.ax.plot([x, x,], [y, 0], [z, 0])
#         #     self.ax.plot([x, 0,], [y, y], [z, 0])
#         #     self.ax.plot([x, 0,], [y, 0], [z, z])
#         self.ax.plot([p1[0], p2[0]],
#                     [p1[1], p2[1]],
#                     [p1[2], p2[2]]
#                     , color='green')
#         self.ax.plot([0, xProj[0]],
#                     [0, xProj[1]],
#                     [0, xProj[2]]
#                     , color='red')

#         self.ax.set_xlabel("X")
#         self.ax.set_ylabel("Y")
#         self.ax.set_zlabel("Z")

class ImageProjectionCanvas(FigureCanvasQTAgg):
    def __init__(self):
        # self.fig = Figure(figsize=(8, 6), dpi=100)
        self.fig = Figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')
        super(ImageProjectionCanvas, self).__init__(self.fig)
        p1 = (0, 0, 0)
        p2 = (3, 4, 10)
        x, y, z = zip(p1, p2)
        self.ax.plot(x, y, z)

        # self.ax.set_xlim([-5, 5])
        # self.ax.set_ylim([-5, 5])
        # self.ax.set_zlim([-20, 20])

        self._drawProjection(p1, p2)

        self.ax.plot([p1[0], p2[0]],
                    [p1[1], p2[1]],
                    [p1[2], p2[2]]
                    , color='green')
        # self.ax.plot([0, xProj[0]],
        #             [0, xProj[1]],
        #             [0, xProj[2]]
        #             , color='red')
        self._configBasicAxe()


    def _drawProjection(self, p1, p2):
        for direction in range(3):
            v = np.zeros(3)
            v[direction] = 1

            # np.dot(a, b) give you lenght of vector
            p1Proj = np.dot(p1, v) * v
            p2Proj = np.dot(p2, v) * v
            self.ax.plot([p1Proj[0], p2Proj[0]],
                        [p1Proj[1], p2Proj[1]],
                        [p1Proj[2], p2Proj[2]]
                        , color='blue')

    def _drawPlaneXY(self):
        xx, yy = np.meshgrid(
            np.linspace(-5, 5, 100),
            np.linspace(-5, 5, 100),
        )
        self.ax.plot_surface(xx,
                            yy,
            # xx - yy
            # 0.12 * xx + 0.01 * y
            0.0001 * xx
            # xx

            #                 np.ones(
            #     shape=(3,3)
            # ) * p2[2]
        )


    def _configBasicAxe(self):
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")
