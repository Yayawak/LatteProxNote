import numpy as np
import cv2
class ImageOrientation:
    def __init__(self):
        ...

    def calculate_moments(self, image):
        moments = cv2.moments(image)
        # second-order moments (central moments
        try:
            self.x_bar = moments['m10'] / moments['m00']
            self.y_bar = moments['m01'] / moments['m00']
            mu11 = np.array(moments['mu11'])
            mu20 = np.array(moments['mu20'])
            mu02 = np.array(moments['mu02'])

            theta = 0.5 * np.arctan(np.divide(2 * mu11, mu20 - mu02))
            self.theta_deg = np.degrees(theta)

            h, w = image.shape[:2]

            if not np.isnan(theta):
                self.x_endline = int(self.x_bar + 0.5 * h * np.tan(theta))
            else:
                self.x_endline = 0
            self.y_endline = h
        # divide zero in moments
        except ArithmeticError:
            pass
            # raise




