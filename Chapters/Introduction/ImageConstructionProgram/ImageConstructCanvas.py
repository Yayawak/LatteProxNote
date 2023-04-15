from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

class ImageConstructCanvas(FigureCanvasQTAgg):
    def __init__(self):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")

        # self.ax.set_xticks([])
        # self.ax.set_yticks([])
        # self.ax.set_zticks([])
        self.camPos = np.array((10, 10, 10))
        self.pointCamPass = np.array((0, 0, 0))
        # self.camPos = np.array((3, 3, 3))
        # self.pointCamPass = np.array((6, 8, 5))
        self.f = 3
        self.ax.plot(*[
            [self.camPos[i], self.pointCamPass[i]]
            for i in range(3)])
        vertices = [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
        ]
        vertices = np.array(vertices)
        edges = [
            (0, 1),
            (0, 2),
            (0, 4),
            # (1, 3),
            (1, 2),
            # (2, 2),
            # (4, 3),
        ]
        edges = np.array(edges)
        x, y, z = zip(*vertices)
        self.ax.scatter(x, y, z)

        vec = self.pointCamPass - self.camPos
        direction = (vec) / np.linalg.norm(vec)
        intersection = self.camPos + direction * self.f
        # intersection = self.camPos + direction * 0.2
        planeNormal = direction / np.linalg.norm(direction)
        planeOrigin = self.camPos + planeNormal * self.f
        u, v = np.mgrid[-1:1:11j, -1:1:11j]
        # planePoints = planeOrigin + u[:, None] * 2 \
        #     * planeNormal[0] + v[None, :] * 2 \
        #     * planeNormal[1]
        # planePoints = np.array([
        #     planeOrigin + u[i,j] * 2 * planeNormal[0] + v[i,j] \
        #     * 2 * planeNormal[1]
        #     for i in range(11) for j in range(11)
        # ])
        # print("u shape ", u.shape)
        # print("pn[0] * u shape", (planeNormal[0]*u).shape)
        # xx, yy, zz = planeOrigin + planeNormal[0]*u + planeNormal[1]*v
        # xx, yy, zz = planeNormal[0]*u + planeNormal[1]*v
        z = (-direction[0] * u - direction[1] * v + self.camPos.dot(direction)) \
            * 1. / direction[2]
        # print("shape z : ", planePoints[:2].shape)
        self.ax.plot_surface(
        # self.ax.plot_trisurf(
            # xx, yy, zz,
            u, v, z,
            # planePoints[:,0],
            # planePoints[:,1],
            # planePoints[:,2],
            color='gray',
            alpha=.5)

        self.ax.plot(*[
            # (self.camPos[i], intersection[i])
            (self.camPos[i], self.pointCamPass[i])
            for i in range(3)
        ])
        for e in edges:
            # line = [(vertices[e[0]][i], vertices[e[1]][i]) for i in range(3)]
            self.ax.plot(*zip(vertices[e[0]], vertices[e[1]]))
