import cv2 as cv
import os
from detector.stringifier import Stringifier
import numpy as np
from ultralytics import YOLO

from PyQt5.QtGui import QPixmap, QImage


class ImageLoader(Stringifier):
    def __init__(self, image: cv.typing.MatLike | str):
        """
        Opens the image
        :param image:
        """
        if type(image) is str:
            self._image = cv.imread(image)
        elif type(image) is cv.typing.MatLike or np.ndarray:
            self._image = image
        else:
            raise TypeError

        # directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', 'test.png')
        # self._cropped_image = cv.imread(directory)
        yolo_cls = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'classify', 'cls_n_100e_only_letters.pt')
        yolo_det = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'detect', 'det_s_100e.pt')
        super().__init__(self._image, model='matching', cls_model=yolo_cls, det_model=yolo_det)

    @staticmethod
    def _to_qimage(image: cv.typing.MatLike) -> QImage:
        frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        return QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)

    def get_image(self) -> QPixmap:
        """
        Returns image as QPixmap
        :return:
        """
        return QPixmap.fromImage(self._to_qimage(self._image))

    def get_cropped_image(self) -> QPixmap:
        """
        Returns 520 x 112 or 0.5, 0.25 scaled size image as QPixmap
        :return:
        """
        return QPixmap.fromImage(self._to_qimage(super().get_cropped_image()))

    # def get_symbols(self) -> str:
    #     """
    #     Returns license plate recognized symbols as string
    #     :return:
    #     """
    #     return a.get_result()
