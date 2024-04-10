import cv2 as cv


class Stringifier:
    def __init__(self, image: cv.typing.MatLike, model: str = 'debug'):
        self._result = None
        if model == 'debug':
            self._model = model
            self._result = 'A000AA116'
        elif model == 'matching':
            self._model = model
        else:
            raise ValueError('Model must be either debug or matching')
        self._image = image

    def __get_result(self):
        return self._result
