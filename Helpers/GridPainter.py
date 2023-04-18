from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             )
from PyQt5.QtGui import QPixmap, QPainter, QPen, QMouseEvent
from PyQt5.QtCore import Qt
import numpy as np

class GridPainter(QWidget):
    # def __init__(self, image_px_cols, image_px_rows, subgrid_size):
    def __init__(self, image_px_cols, image_px_rows):

        super().__init__()
        self.cols = image_px_cols
        self.rows = image_px_rows
        # self.subgrid_size = subgrid_size
        # self.cols = 5
        # self.rows = 3
        self.grid = np.zeros(shape=(self.rows, self.cols), dtype=int)
        self.is_on_draw_mode = True


    def paintEvent(self, ev):
        painter = QPainter(self)
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        painter.setPen(pen)

        # self.cell_w = self.cell_h = self.subgrid_size
        self.cell_w = self.width() * .7 // self.cols
        self.cell_h = self.height() // self.rows
        offset = 0
        for r in range(self.rows):
            for c in range(self.cols):
                color = Qt.black if self.grid[r, c] == 1 else Qt.gray
                x = r * self.cell_w + offset
                y = c * self.cell_h + offset
                painter.fillRect(
                    y, x,
                    # x, y
                    self.cell_w, self.cell_h,
                    color)

    def mouseReleaseEvent(self, ev):
        if ev.button() == Qt.RightButton:
            self.is_on_draw_mode = not self.is_on_draw_mode
            # print("is up pen = ", self.is_on_draw_mode)
            self.setCursor(Qt.PointingHandCursor) if not self.is_on_draw_mode \
                else self.setCursor(Qt.CrossCursor)
            self.update()

    def mousePressEvent(self, ev: QMouseEvent):
        if ev.button() == Qt.LeftButton:
            if not self.is_on_draw_mode:
                self.update_cell(ev.pos(), True)
            else:
                self.update_cell(ev.pos(), False)

    def mouseMoveEvent(self, ev: QMouseEvent):
        if not self.is_on_draw_mode:
            self.update_cell(ev.pos(), True)
        else:
            self.update_cell(ev.pos(), False)

    def update_cell(self, pos, is_white: bool):
        # x = int(pos.x() // self.cell_w)
        # y = int(pos.y() // self.cell_h)
        x = int(pos.x() // self.cell_h)
        y = int(pos.y() // self.cell_w)
        # if 0 <= x < self.rows and 0 <= y < self.cols:
        if 0 <= x < self.cols and 0 <= y < self.rows:
            # self.grid[x][y] = int(is_white)
            self.grid[y][x] = int(is_white)
            self.update()
            # print(self.get_image_grid())

    def get_image_grid(self):
        return self.grid


    def reset_grid(self):
        self.grid = np.zeros(shape=(self.rows, self.cols), dtype=int)
        self.update()
