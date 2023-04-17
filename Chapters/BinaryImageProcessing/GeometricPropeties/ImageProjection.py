import numpy as np


class ImageProjection:
    static_bin_image = np.array([])
    @staticmethod
    def projectionH():
        return np.sum(ImageProjection.static_bin_image, axis=1).T
    @staticmethod
    def projectionV():
        return np.sum(ImageProjection.static_bin_image, axis=0)
