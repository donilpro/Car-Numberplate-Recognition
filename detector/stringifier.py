import cv2 as cv
from detector.detect import detect
from detector.classify import classify
from ultralytics import YOLO


class Stringifier:
    def __init__(self, image: cv.typing.MatLike, model: str = 'debug', cls_model: str = None, det_model: str = None):
        self._result = None
        self._image = image
        if model == 'debug':
            self._model = model
            self._result = 'A000AA116'
        elif model == 'matching':
            self._det_model = YOLO(det_model)
            self._cls_model = YOLO(cls_model)
        else:
            raise ValueError('Model must be either debug or matching')

    def _detect(self):
        self._cropped_image, self._bbox, self._conf, self._det_time = detect(self._image, self._det_model)

    def _classify(self):
        self._result = classify(self._cropped_image, self._cls_model)

    def get_time(self):
        return self._det_time

    def get_conf(self):
        return self._conf

    def get_bbox(self):
        return self._bbox

    def get_cropped_image(self):
        self._detect()
        return self._cropped_image

    def get_symbols(self):
        self._classify()
        return self._result
