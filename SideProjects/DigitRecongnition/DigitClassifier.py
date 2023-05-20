# from DigitRegDemo import DigitRegDemo
# from SideProjects.DigitRecongnition.DigitRegDemo import DigitRegDemo
# import DigitRegDemo
from sklearn.cluster import  KMeans
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import  DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, silhouette_score, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

class DigitClassifier:
    path_dir = os.path.dirname(os.path.abspath(__file__))
    one_path_dir = os.path.join(path_dir, "digits/ones")
    def __init__(self):
        ...
        X = DigitClassifier.load_images_from_folder(DigitClassifier.one_path_dir)
        # print("X", X)
        # self.model = KMeans(2)
        # self.model = LogisticRegression()
        # self.model = SVC(kernel='linear')
        # self.model = LinearRegression()
        self.model = DecisionTreeClassifier()
        # img_height_px, img_width_px = X[0].shape
        X_flatten_all_images = np.array([x.flatten() for x in X])
        # digit_images_flat = X.reshape(len(X), -1)
        # digit_images_flat = X.reshape(len(X), 10 * 10)
        # digit_images_flat = X.reshape(len(X), img_height_px * img_width_px)
        # digit_images_flat = X.reshape(len(X), img_height_px * img_width_px)
        # digit_images_flat = X.flatten()
        # np.flatiter()
        # print("new shape = ", digit_images_flat.shape)
        print("new shape = ", X_flatten_all_images.shape)
        print(X_flatten_all_images)

        Y = np.ones(len(X))
        Y[0] = 0
        # Y[1] = 2
        print("shape of Y", Y.shape)

        self.model.fit(X_flatten_all_images, Y)

        labels = self.model.predict(X_flatten_all_images)
        print("labels", labels)
        score = silhouette_score(X_flatten_all_images, labels)
        print("Silhoette score : ", score)
        # accuracy = accuracy_score()


    # def predict_if_that_is_digit_one(self, bin_image_2d):
    def predict_if_that_is_digit_one(self, bin_image_2d) -> int:

        # X_test = X_flatten_all_images[0].reshape(-1, 100)
        def vectorize():
            return bin_image_2d.reshape(-1, 100)
        X_test = vectorize()
        # X_test = np.zeros((1, 100))

        pred_z_just_one_image = self.model.predict(X_test)
        print("predicted digit label of", X_test.reshape(*bin_image_2d.shape))
        print("result is ", pred_z_just_one_image)
        # pred_z = self.model.predict(X_flatten_all_images)
        return pred_z_just_one_image[0]

    # pred()
    def bin_images_show(self):
        ones_images = self.load_images_from_folder(DigitClassifier.one_path_dir)
        print(ones_images[-1])
        n_images = len(ones_images)
        print("len of images = ", n_images)
        cols = 4
        rows = int(np.ceil(n_images / cols))
        fig, axs = plt.subplots(rows, cols)
        axs_flat = axs.flat
        for i in range(n_images):
            axs_flat[i].imshow(ones_images[i])
            axs_flat[i].set_title(f"images {i}")
        plt.show()
    @staticmethod
    def load_images_from_folder(folder):
        # images = list(npt.ArrayLike)
        images = list()
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename),
                             cv2.IMREAD_GRAYSCALE)
            threshold_value = 127
            ret, bin_img = cv2.threshold(img, threshold_value, 1, cv2.THRESH_BINARY)
            if bin_img is not None:
                images.append(bin_img)
        return np.array(images)

