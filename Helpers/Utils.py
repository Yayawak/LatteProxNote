import numpy as np
from PyQt5.QtGui import QImage, QPixmap

def pixMapToArray(qPix):
    if qPix.isNull() or qPix.width() <= 0 or qPix.height() <= 0:
        raise ValueError("Invalid image dimension")
    image = qPix.toImage()
    bufferPtr = image.bits()
    s = image.bits().asstring(
        image.width() * image.height() * 4
    )
    arr = np.fromstring(s, dtype=np.uint8) \
        .reshape(
            image.width(),
            image.height(),
            4
        )
    # print(arr.shape)
    return arr
    # return arr

def imgArrToPixmap(imgArr):
    h, w, channels = imgArr.shape
    # h, w  = imgArr.shape
    # channels = 4
    qImage = QImage(imgArr.data, w, h, channels * w,
                    # QImage.Format_BGR888)
                    QImage.Format_RGB888)
    return QPixmap().fromImage(qImage)


def rgbaToGray(rgba):
    r, g, b, a = rgba
    # r, g, b = rgba
    # print(rgba)

    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # gray = (y, y, y)
    # if len(rgba) == 4:
        # gray += (255,)

    return y
