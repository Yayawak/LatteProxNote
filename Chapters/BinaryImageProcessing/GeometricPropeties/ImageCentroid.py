import numpy as np
import cv2
class ImageCentroiding:
    @staticmethod
    # def find_centroid(self, image):
    def find_centroid(image):

        # _, thresh = cv2.threshold(self.image, 127, 1, cv2.THRESH_BINARY)
        _, thresh = cv2.threshold(image, 0.5, 1, cv2.THRESH_BINARY)
        # print("")
        M = np.sum(thresh)
        print("np.sum(thresh) =", M)
        # rows, cols = thresh.shape
        rows, cols = np.indices(thresh.shape)
        Mx = np.sum(cols * thresh)
        My = np.sum(rows * thresh)
        if M == 0: return 0, 0
        cx, cy = int(Mx / M), int(My / M)

        return cx, cy
