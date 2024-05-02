import cv2 as cv
from detect import detect
from classify import classify
from ultralytics import YOLO


class Stringifier:
    def __init__(self, image: cv.typing.MatLike, model: str = 'debug', cls_model: YOLO = None, det_model: YOLO = None):
        self._result = None
        self._image = image
        if model == 'debug':
            self._model = model
            self._result = 'A000AA116'
        elif model == 'matching':
            self._det_model = det_model
            self._cls_model = cls_model
        else:
            raise ValueError('Model must be either debug or matching')

    def _detect(self):
        self._cropped_image = detect(self._image, self._det_model)

    def _classify(self):
        self._result = classify(self._cropped_image, self._cls_model)

    def __get_result(self):
        self._detect()
        self._classify()
        return self._result
